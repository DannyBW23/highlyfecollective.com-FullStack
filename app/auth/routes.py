
from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from app.auth.email import send_mail
from sqlalchemy import func

@bp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash(('Invalid username or password'))
			return redirect(url_for('auth.login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('main.index')
		return redirect(next_page)
	return render_template('auth/login.html', title=('Sign In'), form=form)


@bp.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		existing_user = User.query.filter(func.lower(User.username) == func.lower(form.username.data)).first()
		if existing_user:
				flash('Username is already taken. Please choose a different one.')
				return redirect(url_for('auth.register'))

		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)	
		user_with_id_1 = User.query.get(1)


		user.text_input = user_with_id_1.text_input		
		user.text_input1 = user_with_id_1.text_input1
		user.text_input2 = user_with_id_1.text_input2
		user.text_input3 = user_with_id_1.text_input3		
		user.text_input4 = user_with_id_1.text_input4
		user.text_input5 = user_with_id_1.text_input5
		user.text_input6 = user_with_id_1.text_input6
		user.text_input7 = user_with_id_1.text_input7
		user.text_input8 = user_with_id_1.text_input8		
		user.text_input9 = user_with_id_1.text_input9
		user.text_input10 = user_with_id_1.text_input10
		user.text_input11 = user_with_id_1.text_input11
		user.text_input12 = user_with_id_1.text_input12
		user.text_input13 = user_with_id_1.text_input13		
		user.text_input14 = user_with_id_1.text_input14
		user.text_input15 = user_with_id_1.text_input15
		user.text_input16 = user_with_id_1.text_input16
		user.text_input17 = user_with_id_1.text_input17
		user.text_input18 = user_with_id_1.text_input18		
		user.text_input19 = user_with_id_1.text_input19
		user.texts_input = user_with_id_1.texts_input		
		user.texts_input1 = user_with_id_1.texts_input1
		user.texts_input2 = user_with_id_1.texts_input2
		user.texts_input3 = user_with_id_1.texts_input3		
		user.texts_input4 = user_with_id_1.texts_input4
		user.texts_input5 = user_with_id_1.texts_input5
		user.texts_input6 = user_with_id_1.texts_input6
		user.texts_input7 = user_with_id_1.texts_input7
		user.texts_input8 = user_with_id_1.texts_input8		
		user.texts_input9 = user_with_id_1.texts_input9
		user.texts_input10 = user_with_id_1.texts_input10
		user.texts_input11 = user_with_id_1.texts_input11
		user.texts_input12 = user_with_id_1.texts_input12
		user.texts_input13 = user_with_id_1.texts_input13		
		user.texts_input14 = user_with_id_1.texts_input14
		user.texts_input15 = user_with_id_1.texts_input15
		user.texts_input16 = user_with_id_1.texts_input16
		user.texts_input17 = user_with_id_1.texts_input17
		user.texts_input18 = user_with_id_1.texts_input18		
		user.texts_input19 = user_with_id_1.texts_input19
		user.tuxts_input = user_with_id_1.tuxts_input	
		user.tuxts_input1 = user_with_id_1.tuxts_input1
		user.tuxts_input2 = user_with_id_1.tuxts_input2
		user.tuxts_input3 = user_with_id_1.tuxts_input3		
		user.tuxts_input4 = user_with_id_1.tuxts_input4
		user.tuxts_input5 = user_with_id_1.tuxts_input5
		user.tuxts_input6 = user_with_id_1.tuxts_input6
		user.tuxts_input7 = user_with_id_1.tuxts_input7
		user.tuxts_input8 = user_with_id_1.tuxts_input8		
		user.tuxts_input9 = user_with_id_1.tuxts_input9
		user.tuxts_input10 = user_with_id_1.tuxts_input10
		user.tuxts_input11 = user_with_id_1.tuxts_input11
		user.tuxts_input12 = user_with_id_1.tuxts_input12
		user.tuxts_input13 = user_with_id_1.tuxts_input13		
		user.tuxts_input14 = user_with_id_1.tuxts_input14
		user.tuxts_input15 = user_with_id_1.tuxts_input15
		user.tuxts_input16 = user_with_id_1.tuxts_input16
		user.tuxts_input17 = user_with_id_1.tuxts_input17
		user.tuxts_input18 = user_with_id_1.tuxts_input18		
		user.tuxts_input19 = user_with_id_1.tuxts_input19
		db.session.add(user)
		db.session.commit()
		flash(('Congratulations, you are now a registered user!'))
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', title=('Register'),form=form)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form = ResetPasswordRequestForm()
	if form.validate_on_submit():
		email = form.email.data 
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			html_content = render_template('email/reset_password.html',user=user,token=user.get_reset_password_token(),url_for=url_for)
			send_mail(email, html_content)
			flash(('Check your email for the instructions to reset your password'))
		return redirect(url_for('auth.login'))
	return render_template('auth/reset_password_request.html',title=('Reset Password'), form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	user = User.verify_reset_password_token(token)
	if not user:
		return redirect(url_for('main.index'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		user.set_password(form.password.data)
		db.session.commit()
		flash(('Your password has been reset.'))
		return redirect(url_for('auth.login'))	
	return render_template('auth/reset_password.html', form=form)
#e