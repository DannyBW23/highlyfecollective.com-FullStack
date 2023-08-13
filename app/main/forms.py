from flask import request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User


class EditProfileForm(FlaskForm):
	username = StringField(('Username'), validators=[DataRequired()])
	about_me = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])
	profile_pic = FileField("Profile Pic")
	submit = SubmitField("Submit")



	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username
	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError(('Please use a different username.'))


class PicsForm(FlaskForm):
    pics=FileField('pics')
    pics_1=FileField('pics_1')
    pics_2=FileField('pics_2')
    pics_3=FileField('pics_3')
    pics_4=FileField('pics_4')
    pics_5=FileField('pics_5')

    submit = SubmitField('Submit')
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
class NewForm(FlaskForm):
    text_input11 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])   
    text_input10 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input9 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input8 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input7 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input6 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input5 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input4 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input3 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input2 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input1 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
class PostForm(FlaskForm):
    post = TextAreaField(('Say something!'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))

class SearchForm(FlaskForm):
	searched = StringField("Searched", validators=[DataRequired()])
	submit = SubmitField("Submit")
class MessageForm(FlaskForm):
    message = TextAreaField(('Message'), validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(('Submit')) 