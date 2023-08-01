from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app, g, Response
from flask_login import current_user,login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app import db
from app.main.forms import EditProfileForm,EmptyForm, PostForm, SearchForm
from app.models import User, Post
from PIL import Image
import uuid
import os
from app.main import bp
from flask_sqlalchemy import Pagination 
from sqlalchemy import or_
import boto3
from botocore.exceptions import ClientError
from sqlalchemy import func
from http import HTTPStatus
from typing import Optional
def https_redirect() -> Optional[Response]:
    if request.scheme == 'http':
        return redirect(url_for(request.endpoint,_scheme='https',_external=True),HTTPStatus.PERMANENT_REDIRECT)
if current_app.env == 'production':
	current_app.before_request(https_redirect)

@bp.before_app_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@bp.route('/studio', methods=['GET'])
@login_required
def studio():
	next_url = url_for('main.studio')
	prev_url = url_for('main.studio')
	return render_template('studio.html', title='studio', next_url=next_url, prev_url=prev_url)



@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
@login_required
def index():
	next_url = url_for('main.index')
	prev_url = url_for('main.index')
	return render_template('index.html', title='Highlyfe', prev_url=prev_url, next_url=next_url)
@bp.route('/posts')
def posts():
	# Grab all the posts from the database
	posts = Post.query.order_by(Post.date_posted)
	return render_template("_posts.html", posts=posts)

@bp.route('/posts/<int:id>')
def post(id):
	post = Post.query.get_or_404(id)
	return render_template('_post.html', post=post)

@bp.context_processor
def base():
	form = SearchForm()
	return dict(form=form)
@bp.route('/search', methods=["GET", "POST"])
def search():
    form = SearchForm()
    posts = Post.query
    if form.validate_on_submit():
        search_query = form.searched.data
        search_query_ilike = f"%{search_query}%" 
        posts = Post.query.filter((Post.body.ilike(search_query_ilike)) | (Post.author.has(func.lower(User.username) == search_query.lower()))).order_by(Post.timestamp.desc()).all()
        return render_template("search.html", form=form, searched=search_query, posts=posts)
    return redirect(url_for('main.explore'))

@bp.route('/', methods=['GET'])
@bp.route('/About_Us', methods=['GET'])
@login_required
def About_Us():
	return render_template('About_Us.html', title='About Us')

@bp.route('/feed', methods=['GET'])
@login_required
def feed():
	form=PostForm()
	page = request.args.get('page', 1, type=int)
	posts=current_user.followed_posts().filter(Post.author != current_user).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
	next_url = url_for('main.feed', page=posts.next_num) if posts.has_next else None
	prev_url = url_for('main.feed', page=posts.prev_num) if posts.has_prev else None
	return render_template('feed.html', title='feed',form=form, posts=posts.items,next_url=next_url,prev_url=prev_url,user=current_user)
@bp.route('/explore', methods=['GET', 'POST'])
@login_required
def explore():
	page = request.args.get('page', 1, type=int)
	form=PostForm()
	posts = Post.query.order_by(Post.pinned.desc(),Post.timestamp.desc()).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'],error_out=False)			
	next_url = url_for('main.explore', page=posts.next_num) if posts.has_next else None
	prev_url = url_for('main.explore', page=posts.prev_num) if posts.has_prev else None
	if form.validate_on_submit():
		if len(form.post.data) <= 140:
			post = Post(body=form.post.data, author=current_user)
			db.session.add(post) 
			db.session.commit()
			return redirect(url_for('main.explore'))
		else:
			flash("Post length can not exceed 140 characters")
			return redirect(url_for('main.explore'))
	return render_template("explore.html",title='Explore', form=form,user=current_user,posts=posts,next_url=next_url,prev_url=prev_url)



@bp.route('/posts/delete/<int:id>', methods=['POST'])
@login_required
def delete_post(id):
	post_to_delete = Post.query.get_or_404(id)
	current_user_id = current_user.id
	if current_user_id == post_to_delete.author.id or current_user_id == 1:
		try: 
			db.session.delete(post_to_delete)
			db.session.commit()
			posts = Post.query.order_by(Post.timestamp.desc()).all()
			return redirect(request.referrer or url_for('main.explore'))
		except: 
			flash("Whoops! There was a problem deleting post, try again...")
			posts = Post.query.order_by(Post.timestamp.desc()).all()
			return redirect(request.referrer or url_for('main.explore'))
                             #test #test
@bp.route('/user/<username>')
@login_required
def user(username):
	id = current_user.id
	name_to_update = User.query.get_or_404(id)
	user = User.query.filter_by(username=username).first_or_404()
	page = request.args.get('page', 1, type=int)
	posts = user.posts.order_by(Post.timestamp.desc()).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
	next_url = url_for('main.user', username=user.username, page=posts.next_num) if posts.has_next else None
	prev_url = url_for('main.user', username=user.username, page=posts.prev_num) if posts.has_prev else None
	form = EmptyForm()
	return render_template('user.html', user=user, posts=posts.items,form=form, next_url=next_url, prev_url=prev_url,  user_to_delete=name_to_update)
@bp.route('/edit_profile/<username>', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
	form = EditProfileForm(current_user.username)
	id = current_user.id
	name_to_update = User.query.get_or_404(id)
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		if request.files['profile_pic']:
			file = request.files['profile_pic']
			pic_filename = secure_filename(file.filename)
			pic_name = str(uuid.uuid1()) + "_" + pic_filename
			s3_client = boto3.client('s3', region_name='us-east-1')
			try:
				s3_client = boto3.client('s3')
				s3_client.upload_fileobj(file, 'profilepic23', pic_name)
				name_to_update.profile_pic = pic_name # else: e
				db.session.commit()
				return redirect(url_for('main.user', username=username))
			except ClientError as e:
				print(f"Error uploading file to AWS S3: {e}")
				flash("Error!  Looks like there was a problem...try again!")
				return render_template("edit_profile.html", form=form, name_to_update=name_to_update, id=id)
		if len(form.username.data) <= 20:
			current_user.username = form.username.data
			db.session.commit()
			return redirect(url_for('main.user', username=current_user.username))
		else:
			flash("Username length cannot exceed 20 characters")
			return render_template('edit_profile.html', title='Edit Profile',form=form,name_to_update= name_to_update,id=id)
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', title='Edit Profile',form=form,name_to_update= name_to_update,id=id, user=current_user)
                
@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
	form = EmptyForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=username).first()
		if user is None:
			flash('User {} not found.'.format(username))
			return redirect(url_for('main.explore'))
		if user == current_user:
			flash('You cannot follow yourself!')
			return redirect(url_for('main.user', username=username))
		current_user.follow(user)
		db.session.commit()
		flash('You are following!'.format(username))
		return redirect(url_for('main.user', username=username))
	flash('Form validation failed.')   
	return redirect(url_for('main.explore'))
@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
	form = EmptyForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=username).first()
		if user is None:
			flash('User not found.'.format(username))
			return redirect(url_for('main.explore'))
		if user == current_user:
			flash('You cannot unfollow yourself!')
			return redirect(url_for('user', username=username))
		current_user.unfollow(user)
		db.session.commit()
		flash('You are not following'.format(username)) 
		return redirect(url_for('main.user', username=username))
	flash('Form validation failed.')
	return redirect(url_for('main.explore'))
                        
@bp.route('/posts/pin/<int:id>', methods=['POST'])
@login_required
def pin_post(id):
	post = Post.query.get_or_404(id)
	if current_user.id == 1:
		post.pinned = True
		db.session.commit()
	else:
		flash("You are not authorized to pin this post.")
	return redirect(url_for('main.explore'))
                
@bp.route('/posts/unpin/<int:id>', methods=['POST'])
@login_required
def unpin_post(id):
	post = Post.query.get_or_404(id)
	if current_user.id == 1:
		post.pinned = False
		db.session.commit()
	else:
		flash("You are not authorized to unpin this post.")
	return redirect(url_for('main.explore'))
        
@bp.route('/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete(id):
	if id == current_user.id or  current_user.id==1 :
		user_to_delete = User.query.get_or_404(id)
		name = None
		form = EditProfileForm(current_user.username)
		try:
			db.session.delete(user_to_delete)
			db.session.commit()
			flash("User Deleted Successfully!!")
			our_users = User.query.all()
			return redirect(url_for('main.explore'))
   			#return render_template("edit_profile.html", form=form, name=name, our_users=our_users,name_to_update=user_to_delete)

		except:
			flash("Whoops! There was a problem deleting the user. Please try again...")
			our_users  = User.query.all()
			return render_template("edit_profile.html", form=form, name=name, our_users=our_users, name_to_update=user_to_delete)
                
	else:
		flash("Sorry, you can't delete that user!")     
	return redirect(url_for('main.edit_profile'))
#ee#ee
@bp.route('/posts/action/<int:id>/<action>', methods=['POST'])
@login_required
def post_action(id, action):
	post = Post.query.get_or_404(id)
	if action == 'delete':
		if post.user_id == current_user.id or current_user.id == 1:
			try:
				db.session.delete(post)
				db.session.commit()
			except:
				flash("Whoops! There was a problem deleting the post.")
		else:
			flash("You are not authorized to delete this post.")
	elif action == 'pin':
		if current_user.id == 1:
			post.pinned = True
			db.session.commit()
		else:
			flash("You are not authorized to pin posts.")
	else:
		flash("Invalid action.")
	return redirect(url_for('main.explore'))     
@bp.route('/followers/<username>')
@login_required
def followers(username):
	page = request.args.get('page', 1, type=int)
	per_page = 3
	user = User.query.filter_by(username=username).first_or_404()
	followers = user.followers.paginate(page=page, per_page=per_page)
	prev_url = None 
	if followers.has_prev:
		prev_url = url_for('main.followers', username=username, page=followers.prev_num)
	next_url = None
	if followers.has_next:
		next_url = url_for('main.followers', username=username, page=followers.next_num)
	return render_template('followers.html', title='Following', user=user, followers=followers, prev_url=prev_url, next_url=next_url)
@bp.route('/following/<username>')
@login_required
def following(username):
	page = request.args.get('page', 1, type=int)
	per_page = 2
	user = User.query.filter_by(username=username).first_or_404()
	following = user.followed.paginate(page=page, per_page=per_page)
	prev_url = None 
	if following.has_prev:
		prev_url = url_for('main.following', username=username, page=following.prev_num)
	next_url = None
	if following.has_next:
		next_url = url_for('main.following', username=username, page=following.next_num)
	return render_template('following.html', title='Following', user=user, following=following, prev_url=prev_url, next_url=next_url)