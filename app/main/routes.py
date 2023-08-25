from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app
from flask_login import current_user,login_required
from werkzeug.utils import secure_filename
from app import db
from app.main.forms import EditProfileForm,EmptyForm, PostForm, SearchForm, MessageForm, NewForm, PicsForm, NewsForm, PicForm, PitForm,NuwsForm
from app.models import User, Post, Message, Notification
import uuid
from app.main import bp
from flask_sqlalchemy import Pagination 
import boto3
from botocore.exceptions import ClientError
from sqlalchemy import func
from app.auth.forms import LoginForm
@bp.before_app_request
def before_request():
	if not request.is_secure:
		if not current_user.is_authenticated:
			url = request.url.replace("http://", "https://", 1)
			return redirect(url, code=301)
	if not request.is_secure:
		if current_user.is_authenticated:
			url = request.url.replace("http://", "https://", 1)
			current_user.last_seen = datetime.utcnow()
			db.session.commit()
			return redirect(url, code=301)
	if request.is_secure:
		if current_user.is_authenticated:
			current_user.last_seen = datetime.utcnow()
			db.session.commit()	
@bp.route('/studio', methods=['GET','POST'])
@login_required
def studio():
	form=PicForm()
	forms=NewsForm()
	id = current_user.id
	users = User.query.all()
	name_to_update = User.query.get_or_404(id)

	if forms.validate_on_submit() :
		texts_input = forms.texts_input.data
		texts_input1 = forms.texts_input1.data
		texts_input2 = forms.texts_input2.data
		texts_input3 = forms.texts_input3.data
		texts_input4 = forms.texts_input4.data
		texts_input5 = forms.texts_input5.data
		texts_input6 = forms.texts_input6.data
		texts_input7 = forms.texts_input7.data
		texts_input8 = forms.texts_input8.data
		texts_input9 = forms.texts_input9.data
		texts_input10 = forms.texts_input10.data
		texts_input11 = forms.texts_input11.data
		texts_input12 = forms.texts_input12.data
		texts_input13 = forms.texts_input13.data
		texts_input14 = forms.texts_input14.data
		texts_input15 = forms.texts_input15.data
		texts_input16 = forms.texts_input16.data
		texts_input17 = forms.texts_input17.data
		texts_input18 = forms.texts_input18.data
		texts_input19 = forms.texts_input19.data
		db.session.commit()
		if texts_input:
			for user in users:
				texts_input = forms.texts_input.data
				user.texts_input = texts_input
				db.session.commit()

		if texts_input1:
			for user in users:
				texts_input1 = forms.texts_input1.data
				user.texts_input1 = texts_input1
				db.session.commit()
		if texts_input2:
			for user in users:
				texts_input2 = forms.texts_input2.data
				user.texts_input2 = texts_input2
				db.session.commit()
		if texts_input3:
			for user in users:
				texts_input3 = forms.texts_input3.data
				user.texts_input3 = texts_input3
				db.session.commit()
		if texts_input4:
			for user in users:
				texts_input4 = forms.texts_input4.data
				user.texts_input4= texts_input4
				db.session.commit()
		if texts_input5:
			for user in users:
				texts_input5 = forms.texts_input5.data
				user.texts_input5 = texts_input5
				db.session.commit()
		if texts_input6:
			for user in users:
				texts_input6 = forms.texts_input6.data
				user.texts_input6 = texts_input6
				db.session.commit()
		if texts_input7:
			for user in users:
				texts_input7 = forms.texts_input7.data
				user.texts_input7 = texts_input7
				db.session.commit()
		if texts_input8:
			for user in users:
				texts_input8 = forms.texts_input8.data
				user.texts_input8 = texts_input8
				db.session.commit()
		if texts_input9:
			for user in users:
				texts_input9 = forms.texts_input9.data
				user.texts_input9= texts_input9
				db.session.commit()
		if texts_input10:
			for user in users:
				texts_input10 = forms.texts_input10.data
				user.texts_input10 = texts_input10
				db.session.commit()
		if texts_input11:
			for user in users:
				texts_input11 = forms.texts_input11.data
				user.texts_input11 = texts_input11
				db.session.commit()
		if texts_input12:
			for user in users:
				texts_input12 = forms.texts_input12.data
				user.texts_input12 = texts_input12
				db.session.commit()
		if texts_input13:
			for user in users:
				texts_input13 = forms.texts_input13.data
				user.texts_input13 = texts_input13
				db.session.commit()
		if texts_input14:
			for user in users:
				texts_input14 = forms.texts_input14.data
				user.texts_input14= texts_input14
				db.session.commit()
		if texts_input15:
			for user in users:
				texts_input15 = forms.texts_input15.data
				user.texts_input15 = texts_input15
				db.session.commit()
		if texts_input16:
			for user in users:
				texts_input16 = forms.texts_input16.data
				user.texts_input16 = texts_input16
				db.session.commit()
		if texts_input17:
			for user in users:
				texts_input17 = forms.texts_input17.data
				user.texts_input17 = texts_input17
				db.session.commit()
		if texts_input18:
			for user in users:
				texts_input18 = forms.texts_input18.data
				user.texts_input18 = texts_input18
				db.session.commit()
		if texts_input19:
			for user in users:
				texts_input19 = forms.texts_input19.data
				user.texts_input19= texts_input19
				db.session.commit()
	if form.validate_on_submit() :
		if not texts_input and not texts_input1 and not texts_input2 and not texts_input3 and not texts_input4 and not texts_input5 and not texts_input6 and not texts_input7 and not texts_input8 and not texts_input9 and not texts_input10 and not texts_input11 and not texts_input12 and not texts_input13 and not texts_input14 and not texts_input15 and not texts_input16 and not texts_input17 and not texts_input18 and not texts_input19:
			if request.method == 'POST':
				if 'pic' in request.files:
					file = request.files['pic']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form)
				if 'pic_1' in request.files:
					file = request.files['pic_1']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_1 = pic_name 

						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_2' in request.files:
					file = request.files['pic_2']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_2 = pic_name 

						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_3' in request.files:
					file = request.files['pic_3']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_3 = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_4' in request.files:
					file = request.files['pic_4']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_4 = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_5' in request.files:
					file = request.files['pic_5']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_5 = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_6' in request.files:
					file = request.files['pic_6']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_6 = pic_name 

						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_7' in request.files:
					file = request.files['pic_7']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_7 = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_8' in request.files:
					file = request.files['pic_8']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_8 = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pic_9' in request.files:
					file = request.files['pic_9']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pic_9 = pic_name 
						db.session.commit()
						return redirect(url_for('main.studio', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
	return render_template('studio.html',users=users, title='studio', name_to_update=name_to_update, id=id, form=form, forms=forms)
@bp.route('/design', methods=['GET', 'POST'])
@login_required
def design():
	form = LoginForm()
	username = User.query.filter_by(username=form.username.data).first()
	return render_template('design.html', username=username)

@bp.route('/', methods=['GET','POST'])
@bp.route('/index', methods=['GET','POST'])
@login_required
def index():
	form=PitForm()
	forms=NuwsForm()
	id = current_user.id
	users = User.query.all()
	name_to_update = User.query.get_or_404(id)

	if forms.validate_on_submit() :
		tuxts_input = forms.tuxts_input.data
		tuxts_input1 = forms.tuxts_input1.data
		tuxts_input2 = forms.tuxts_input2.data
		tuxts_input3 = forms.tuxts_input3.data
		tuxts_input4 = forms.tuxts_input4.data
		tuxts_input5 = forms.tuxts_input5.data
		tuxts_input6 = forms.tuxts_input6.data
		tuxts_input7 = forms.tuxts_input7.data
		tuxts_input8 = forms.tuxts_input8.data
		tuxts_input9 = forms.tuxts_input9.data
		tuxts_input10 = forms.tuxts_input10.data
		tuxts_input11 = forms.tuxts_input11.data
		tuxts_input12 = forms.tuxts_input12.data
		tuxts_input13 = forms.tuxts_input13.data
		tuxts_input14 = forms.tuxts_input14.data
		tuxts_input15 = forms.tuxts_input15.data
		tuxts_input16 = forms.tuxts_input16.data
		tuxts_input17 = forms.tuxts_input17.data
		tuxts_input18 = forms.tuxts_input18.data
		tuxts_input19 = forms.tuxts_input19.data
		db.session.commit()
		if tuxts_input:
			for user in users:
				tuxts_input = forms.tuxts_input.data
				user.tuxts_input = tuxts_input
				db.session.commit()
		if tuxts_input1:
			for user in users:
				tuxts_input1 = forms.tuxts_input1.data
				user.tuxts_input1 = tuxts_input1
				db.session.commit()
		if tuxts_input2:
			for user in users:
				tuxts_input2 = forms.tuxts_input2.data
				user.tuxts_input2 = tuxts_input2
				db.session.commit()
		if tuxts_input3:
			for user in users:
				tuxts_input3 = forms.tuxts_input3.data
				user.tuxts_input3 = tuxts_input3
				db.session.commit()
		if tuxts_input4:
			for user in users:
				tuxts_input4 = forms.tuxts_input4.data
				user.tuxts_input4= tuxts_input4
				db.session.commit()
		if tuxts_input5:
			for user in users:
				tuxts_input5 = forms.tuxts_input5.data
				user.tuxts_input5 = tuxts_input5
				db.session.commit()
		if tuxts_input6:
			for user in users:
				tuxts_input6 = forms.tuxts_input6.data
				user.tuxts_input6 = tuxts_input6
				db.session.commit()
		if tuxts_input7:
			for user in users:
				tuxts_input7 = forms.tuxts_input7.data
				user.tuxts_input7 = tuxts_input7
				db.session.commit()
		if tuxts_input8:
			for user in users:
				tuxts_input8 = forms.tuxts_input8.data
				user.tuxts_input8 = tuxts_input8
				db.session.commit()
		if tuxts_input9:
			for user in users:
				tuxts_input9 = forms.tuxts_input9.data
				user.tuxts_input9= tuxts_input9
				db.session.commit()
		if tuxts_input10:
			for user in users:
				tuxts_input10 = forms.tuxts_input10.data
				user.tuxts_input10 = tuxts_input10
				db.session.commit()
		if tuxts_input11:
			for user in users:
				tuxts_input11 = forms.tuxts_input11.data
				user.tuxts_input11 = tuxts_input11
				db.session.commit()
		if tuxts_input12:
			for user in users:
				tuxts_input12 = forms.tuxts_input12.data
				user.tuxts_input12 = tuxts_input12
				db.session.commit()
		if tuxts_input13:
			for user in users:
				tuxts_input13 = forms.tuxts_input13.data
				user.tuxts_input13 = tuxts_input13
				db.session.commit()
		if tuxts_input14:
			for user in users:
				tuxts_input14 = forms.tuxts_input14.data
				user.tuxts_input14= tuxts_input14
				db.session.commit()
		if tuxts_input15:
			for user in users:
				tuxts_input15 = forms.tuxts_input15.data
				user.tuxts_input15 = tuxts_input15
				db.session.commit()
		if tuxts_input16:
			for user in users:
				tuxts_input16 = forms.tuxts_input16.data
				user.tuxts_input16 = tuxts_input16
				db.session.commit()
		if tuxts_input17:
			for user in users:
				tuxts_input17 = forms.tuxts_input17.data
				user.tuxts_input17 = tuxts_input17
				db.session.commit()
		if tuxts_input18:
			for user in users:
				tuxts_input18 = forms.tuxts_input18.data
				user.tuxts_input18 = tuxts_input18
				db.session.commit()
		if tuxts_input19:
			for user in users:
				tuxts_input19 = forms.tuxts_input19.data
				user.tuxts_input19= tuxts_input19
				db.session.commit()
	if form.validate_on_submit() :
		if not tuxts_input and not tuxts_input1 and not tuxts_input2 and not tuxts_input3 and not tuxts_input4 and not tuxts_input5 and not tuxts_input6 and not tuxts_input7 and not tuxts_input8 and not tuxts_input9 and not tuxts_input10 and not tuxts_input11 and not tuxts_input12 and not tuxts_input13 and not tuxts_input14 and not tuxts_input15 and not tuxts_input16 and not tuxts_input17 and not tuxts_input18 and not tuxts_input19:
			if request.method == 'POST':
				if 'pit' in request.files:
					file = request.files['pit']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form)
				if 'pit_1' in request.files:
					file = request.files['pit_1']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_1 = pic_name 

						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_2' in request.files:
					file = request.files['pit_2']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_2 = pic_name 

						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_3' in request.files:
					file = request.files['pit_3']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_3 = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_4' in request.files:
					file = request.files['pit_4']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_4 = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("studio.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_5' in request.files:
					file = request.files['pit_5']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_5 = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_6' in request.files:
					file = request.files['pit_6']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_6 = pic_name 

						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_7' in request.files:
					file = request.files['pit_7']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_7 = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_8' in request.files:
					file = request.files['pit_8']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_8 = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pit_9' in request.files:
					file = request.files['pit_9']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pit_9 = pic_name 
						db.session.commit()
						return redirect(url_for('main.index', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("index.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
	return render_template('index.html',users=users, title='highlyfe', name_to_update=name_to_update, id=id, form=form, forms=forms)


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


@bp.route('/About_Us', methods=['GET', 'POST'])
@login_required
def About_Us():
	form=PicsForm()
	forms=NewForm()
	id = current_user.id
	users = User.query.all()
	name_to_update = User.query.get_or_404(id)

	if forms.validate_on_submit() :
		text_input = forms.text_input.data
		text_input1 = forms.text_input1.data
		text_input2 = forms.text_input2.data
		text_input3 = forms.text_input3.data
		text_input4 = forms.text_input4.data
		text_input5 = forms.text_input5.data
		text_input6 = forms.text_input6.data
		text_input7 = forms.text_input7.data
		text_input8 = forms.text_input8.data
		text_input9 = forms.text_input9.data
		text_input10 = forms.text_input10.data
		text_input11 = forms.text_input11.data
		text_input12 = forms.text_input12.data
		text_input13 = forms.text_input13.data
		text_input14 = forms.text_input14.data
		text_input15 = forms.text_input15.data
		text_input16 = forms.text_input16.data
		text_input17 = forms.text_input17.data
		text_input18 = forms.text_input18.data
		text_input19 = forms.text_input19.data
		db.session.commit()
		if text_input:
			for user in users:
				text_input = forms.text_input.data
				user.text_input = text_input
				db.session.commit()
		if text_input1:
			for user in users:
				text_input1 = forms.text_input1.data
				user.text_input1 = text_input1
				db.session.commit()
		if text_input2:
			for user in users:
				text_input2 = forms.text_input2.data
				user.text_input2 = text_input2
				db.session.commit()
		if text_input3:
			for user in users:
				text_input3 = forms.text_input3.data
				user.text_input3 = text_input3
				db.session.commit()
		if text_input4:
			for user in users:
				text_input4 = forms.text_input4.data
				user.text_input4= text_input4
				db.session.commit()
		if text_input5:
			for user in users:
				text_input5 = forms.text_input5.data
				user.text_input5 = text_input5
				db.session.commit()
		if text_input6:
			for user in users:
				text_input6 = forms.text_input6.data
				user.text_input6 = text_input6
				db.session.commit()
		if text_input7:
			for user in users:
				text_input7 = forms.text_input7.data
				user.text_input7 = text_input7
				db.session.commit()
		if text_input8:
			for user in users:
				text_input8 = forms.text_input8.data
				user.text_input8 = text_input8
				db.session.commit()
		if text_input9:
			for user in users:
				text_input9 = forms.text_input9.data
				user.text_input9= text_input9
				db.session.commit()
		if text_input10:
			for user in users:
				text_input10 = forms.text_input10.data
				user.text_input10 = text_input10
				db.session.commit()
		if text_input11:
			for user in users:
				text_input11 = forms.text_input11.data
				user.text_input11 = text_input11
				db.session.commit()
		if text_input12:
			for user in users:
				text_input12 = forms.text_input12.data
				user.text_input12 = text_input12
				db.session.commit()
		if text_input13:
			for user in users:
				text_input13 = forms.text_input13.data
				user.text_input13 = text_input13
				db.session.commit()
		if text_input14:
			for user in users:
				text_input14 = forms.text_input14.data
				user.text_input14= text_input14
				db.session.commit()
		if text_input15:
			for user in users:
				text_input15 = forms.text_input15.data
				user.text_input15 = text_input15
				db.session.commit()
		if text_input16:
			for user in users:
				text_input16 = forms.text_input16.data
				user.text_input16 = text_input16
				db.session.commit()
		if text_input17:
			for user in users:
				text_input17 = forms.text_input17.data
				user.text_input17 = text_input17
				db.session.commit()
		if text_input18:
			for user in users:
				text_input18 = forms.text_input18.data
				user.text_input18 = text_input18
				db.session.commit()
		if text_input19:
			for user in users:
				text_input19 = forms.text_input19.data
				user.text_input19= text_input19
				db.session.commit()
	if form.validate_on_submit() :
		if not text_input and not text_input1 and not text_input2 and not text_input3 and not text_input4 and not text_input5 and not text_input6 and not text_input7 and not text_input8 and not text_input9 and not text_input10 and not text_input11 and not text_input12 and not text_input13 and not text_input14 and not text_input15 and not text_input16 and not text_input17 and not text_input18 and not text_input19:
			if request.method == 'POST':
				if 'pics' in request.files:
					file = request.files['pics']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics = pic_name # else: e
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form)
				if 'pics_1' in request.files:
					file = request.files['pics_1']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_1 = pic_name 

						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_2' in request.files:
					file = request.files['pics_2']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_2 = pic_name 

						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_3' in request.files:
					file = request.files['pics_3']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_3 = pic_name 
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_4' in request.files:
					file = request.files['pics_4']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_4 = pic_name 
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_5' in request.files:
					file = request.files['pics_5']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_5 = pic_name 
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_6' in request.files:
					file = request.files['pics_6']
					pic_filename = secure_filename(file.filename)

					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_6 = pic_name 

						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_7' in request.files:
					file = request.files['pics_7']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_7 = pic_name 
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_8' in request.files:
					file = request.files['pics_8']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_8 = pic_name 
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
				if 'pics_9' in request.files:
					file = request.files['pics_9']
					pic_filename = secure_filename(file.filename)
					pic_name = str(uuid.uuid1()) + "_" + pic_filename
					s3_client = boto3.client('s3', region_name='us-east-1')
					try:
						s3_client = boto3.client('s3')
						s3_client.upload_fileobj(file, 'profilepic23', pic_name)
						name_to_update.pics_9 = pic_name 
						db.session.commit()
						return redirect(url_for('main.About_Us', form=form))
					except ClientError as e:
						print(f"Error uploading file to AWS S3: {e}")
						flash("Error!  Looks like there was a problem...try again!")
						return render_template("About_Us.html", name_to_update=name_to_update, id=id, form=form, forms=forms)
	return render_template('About_Us.html',users=users, title='About Us', name_to_update=name_to_update, id=id, form=form, forms=forms)


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
	if current_user_id == post_to_delete.author.id or current_user_id == 1 or current_user_id == 4:
		try: 
			db.session.delete(post_to_delete)
			db.session.commit()
			posts = Post.query.order_by(Post.timestamp.desc()).all()
			return redirect(request.referrer or url_for('main.explore'))
		except: 
			flash("Whoops! There was a problem deleting post, try again...")
			posts = Post.query.order_by(Post.timestamp.desc()).all()
			return redirect(request.referrer or url_for('main.explore'))
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
		existing_user = User.query.filter(User.username.ilike(form.username.data)).first()
		if existing_user and existing_user.username != current_user.username:	
			flash('Please use a different username.', 'danger')
			return redirect(url_for('main.edit_profile', username=username))
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
	if current_user.id == 1 or current_user.id == 4:
		post.pinned = True
		db.session.commit()
	else:
		flash("You are not authorized to pin this post.")
	return redirect(url_for('main.explore'))
                
@bp.route('/posts/unpin/<int:id>', methods=['POST'])
@login_required
def unpin_post(id):
	post = Post.query.get_or_404(id)
	if current_user.id == 1 or current_user.id == 4:
		post.pinned = False
		db.session.commit()
	else:
		flash("You are not authorized to unpin this post.")
	return redirect(url_for('main.explore'))
        
@bp.route('/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete(id):
	if id == current_user.id or  current_user.id==1 or current_user.id == 4:
		user_to_delete = User.query.get_or_404(id)
		name = None
		form = EditProfileForm(current_user.username)
		try:
			db.session.delete(user_to_delete)
			db.session.commit()
			flash("User Deleted Successfully!!")
			our_users = User.query.all()
			return redirect(url_for('main.explore'))
		except:
			flash("Whoops! There was a problem deleting the user. Please try again...")
			our_users  = User.query.all()
			return render_template("edit_profile.html", form=form, name=name, our_users=our_users, name_to_update=user_to_delete)               
	else:
		flash("Sorry, you can't delete that user!")     
	return redirect(url_for('main.edit_profile'))
@bp.route('/posts/action/<int:id>/<action>', methods=['POST'])
@login_required
def post_action(id, action):
	post = Post.query.get_or_404(id)
	if action == 'delete':
		if post.user_id == current_user.id or current_user.id == 1 or current_user.id == 4:
			try:
				db.session.delete(post)
				db.session.commit()
			except:
				flash("Whoops! There was a problem deleting the post.")
		else:
			flash("You are not authorized to delete this post.")
	elif action == 'pin':
		if current_user.id == 1 or current_user.id == 4:
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
@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
	user = User.query.filter_by(username=recipient).first_or_404()
	form = MessageForm()	
	if form.validate_on_submit():
		msg = Message(author=current_user, recipient=user,body=form.message.data)
		db.session.add(msg)
		user.add_notification('unread_message_count', user.new_messages())
		db.session.commit()
		flash(('Your message has been sent.'))
		return redirect(url_for('main.user', username=recipient))
	return render_template('send_message.html', title=('Send Message'),form=form, recipient=recipient)
@bp.route('/send_message1/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message1(recipient):
	user = User.query.filter_by(username=recipient).first_or_404()
	form = MessageForm()	
	if form.validate_on_submit():
		msg = Message(author=current_user, recipient=user,body=form.message.data)
		db.session.add(msg)
		user.add_notification('unread_message_count', user.new_messages())
		db.session.commit()
		flash(('Your message has been sent.'))
		return redirect(url_for('main.messages', username=recipient))
	return render_template('send_message.html', title=('Send Message'),form=form, recipient=recipient)
@bp.route('/messages/<username>')
@login_required
def messages(username):
	current_user.last_message_read_time = datetime.utcnow()
	current_user.add_notification('unread_message_count', 0)
	db.session.commit()
	user = User.query.filter_by(username=username).first_or_404()
	page = request.args.get('page', 1, type=int)
	messages = current_user.messages_received.order_by(Message.timestamp.desc()).paginate(page=page, per_page=current_app.config['POSTS_PER_PAGE'],error_out=False)
	next_url = url_for('main.messages',username=user.username,page=messages.next_num)if messages.has_next else None
	prev_url = url_for('main.messages',username=user.username,page=messages.prev_num)if messages.has_prev else None
	return render_template('messages.html', messages=messages.items,next_url=next_url, prev_url=prev_url, user=user)
@bp.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications])




