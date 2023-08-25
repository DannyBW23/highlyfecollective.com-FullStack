from flask import request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
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
class PicForm(FlaskForm):
    pic=FileField('pic' ,validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_1=FileField('pic_1',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_2=FileField('pic_2',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_3=FileField('pic_3',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_4=FileField('pic_4',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_5=FileField('pic_5',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_6=FileField('pic_6',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_7=FileField('pic_7',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_8=FileField('pic_8',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pic_9=FileField('pic_9',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    submit = SubmitField('Submit')
class PitForm(FlaskForm):
    pit=FileField('pit',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_1=FileField('pit_1',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_2=FileField('pit_2',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_3=FileField('pit_3',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_4=FileField('pit_4',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_5=FileField('pit_5',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_6=FileField('pit_6',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_7=FileField('pit_7',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_8=FileField('pit_8',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pit_9=FileField('pit_9',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    submit = SubmitField('Submit')
class PicsForm(FlaskForm):
    pics=FileField('pics',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_1=FileField('pics_1',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_2=FileField('pics_2',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_3=FileField('pics_3',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_4=FileField('pics_4',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_5=FileField('pics_5',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_6=FileField('pics_6',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_7=FileField('pics_7',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_8=FileField('pics_8',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    pics_9=FileField('pics_9',validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'mov','mp4','mp3'])])
    submit = SubmitField('Submit')

class NewsForm(FlaskForm):
    texts_input19 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input18 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input17 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input16 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input15 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input14 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input13 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input12 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input11 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])   
    texts_input10 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input9 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input8 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input7 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input6 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input5 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input4 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input3 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input2 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input1 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    texts_input = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
class NuwsForm(FlaskForm):
    tuxts_input19 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input18 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input17 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input16 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input15 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input14 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input13 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input12 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input11 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])   
    tuxts_input10 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input9 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input8 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input7 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input6 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input5 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input4 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input3 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input2 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input1 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    tuxts_input = TextAreaField(('Bio'),validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
class NewForm(FlaskForm):
    text_input19 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input18 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input17 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input16 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input15 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input14 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input13 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
    text_input12 = TextAreaField(('Bio'),validators=[Length(min=0, max=140)]) 
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