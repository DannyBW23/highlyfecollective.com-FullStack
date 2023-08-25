from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt
from app import db, login
import json

followers = db.Table('followers',db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))


class User(UserMixin, db.Model):


	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	profile_pic = db.Column(db.String(255), nullable=True)
	pics=db.Column(db.String(255), nullable=True)
	pics_1=db.Column(db.String(255), nullable=True)
	pics_2=db.Column(db.String(255), nullable=True)
	pics_3=db.Column(db.String(255), nullable=True)
	pics_4=db.Column(db.String(255), nullable=True)
	pics_5=db.Column(db.String(255), nullable=True)
	pics_6=db.Column(db.String(255), nullable=True)
	pics_7=db.Column(db.String(255), nullable=True)
	pics_8=db.Column(db.String(255), nullable=True)
	pics_9=db.Column(db.String(255), nullable=True)
	text_input = db.Column(db.String(200), nullable=True)
	text_input1=db.Column(db.String(200), nullable=True)
	text_input2=db.Column(db.String(200), nullable=True)
	text_input3=db.Column(db.String(200), nullable=True)
	text_input4=db.Column(db.String(200), nullable=True)
	text_input5=db.Column(db.String(200), nullable=True)
	text_input6=db.Column(db.String(200), nullable=True)
	text_input7=db.Column(db.String(200), nullable=True)
	text_input8=db.Column(db.String(200), nullable=True)
	text_input9=db.Column(db.String(200), nullable=True)
	text_input10=db.Column(db.String(200), nullable=True)
	text_input11=db.Column(db.String(200), nullable=True)
	text_input12=db.Column(db.String(200), nullable=True)
	text_input13=db.Column(db.String(200), nullable=True)
	text_input14=db.Column(db.String(200), nullable=True)
	text_input15=db.Column(db.String(200), nullable=True)
	text_input16=db.Column(db.String(200), nullable=True)
	text_input17=db.Column(db.String(200), nullable=True)
	text_input18=db.Column(db.String(200), nullable=True)
	text_input19=db.Column(db.String(200), nullable=True)
	texts_input = db.Column(db.String(200), nullable=True)
	texts_input1=db.Column(db.String(200), nullable=True)
	texts_input2=db.Column(db.String(200), nullable=True)
	texts_input3=db.Column(db.String(200), nullable=True)
	texts_input4=db.Column(db.String(200), nullable=True)
	texts_input5=db.Column(db.String(200), nullable=True)
	texts_input6=db.Column(db.String(200), nullable=True)
	texts_input7=db.Column(db.String(200), nullable=True)
	texts_input8=db.Column(db.String(200), nullable=True)
	texts_input9=db.Column(db.String(200), nullable=True)
	texts_input10=db.Column(db.String(200), nullable=True)
	texts_input11=db.Column(db.String(200), nullable=True)
	texts_input12=db.Column(db.String(200), nullable=True)
	texts_input13=db.Column(db.String(200), nullable=True)
	texts_input14=db.Column(db.String(200), nullable=True)
	texts_input15=db.Column(db.String(200), nullable=True)
	texts_input16=db.Column(db.String(200), nullable=True)
	texts_input17=db.Column(db.String(200), nullable=True)
	texts_input18=db.Column(db.String(200), nullable=True)
	texts_input19=db.Column(db.String(200), nullable=True)
	picx=db.Column(db.String(255), nullable=True)
	pic_1=db.Column(db.String(255), nullable=True)
	pic_2=db.Column(db.String(255), nullable=True)
	pic_3=db.Column(db.String(255), nullable=True)
	pic_4=db.Column(db.String(255), nullable=True)
	pic_5=db.Column(db.String(255), nullable=True)
	pic_6=db.Column(db.String(255), nullable=True)
	pic_7=db.Column(db.String(255), nullable=True)
	pic_8=db.Column(db.String(255), nullable=True)
	pic_9=db.Column(db.String(255), nullable=True)
	pitx=db.Column(db.String(255), nullable=True)
	pit_1=db.Column(db.String(255), nullable=True)
	pit_2=db.Column(db.String(255), nullable=True)
	pit_3=db.Column(db.String(255), nullable=True)
	pit_4=db.Column(db.String(255), nullable=True)
	pit_5=db.Column(db.String(255), nullable=True)
	pit_6=db.Column(db.String(255), nullable=True)
	pit_7=db.Column(db.String(255), nullable=True)
	pit_8=db.Column(db.String(255), nullable=True)
	pit_9=db.Column(db.String(255), nullable=True)
	tuxts_input = db.Column(db.String(200), nullable=True)
	tuxts_input1=db.Column(db.String(200), nullable=True)
	tuxts_input2=db.Column(db.String(200), nullable=True)
	tuxts_input3=db.Column(db.String(200), nullable=True)
	tuxts_input4=db.Column(db.String(200), nullable=True)
	tuxts_input5=db.Column(db.String(200), nullable=True)
	tuxts_input6=db.Column(db.String(200), nullable=True)
	tuxts_input7=db.Column(db.String(200), nullable=True)
	tuxts_input8=db.Column(db.String(200), nullable=True)
	tuxts_input9=db.Column(db.String(200), nullable=True)
	tuxts_input10=db.Column(db.String(200), nullable=True)
	tuxts_input11=db.Column(db.String(200), nullable=True)
	tuxts_input12=db.Column(db.String(200), nullable=True)
	tuxts_input13=db.Column(db.String(200), nullable=True)
	tuxts_input14=db.Column(db.String(200), nullable=True)
	tuxts_input15=db.Column(db.String(200), nullable=True)
	tuxts_input16=db.Column(db.String(200), nullable=True)
	tuxts_input17=db.Column(db.String(200), nullable=True)
	tuxts_input18=db.Column(db.String(200), nullable=True)
	tuxts_input19=db.Column(db.String(200), nullable=True)
	messages_sent = db.relationship('Message',foreign_keys='Message.sender_id',backref='author', lazy='dynamic')
	messages_received = db.relationship('Message',foreign_keys='Message.recipient_id',backref='recipient', lazy='dynamic')
	last_message_read_time = db.Column(db.DateTime)
	followed = db.relationship('User', secondary=followers,primaryjoin=(followers.c.follower_id == id),secondaryjoin=(followers.c.followed_id == id),backref=db.backref('followers', lazy='dynamic'),lazy='dynamic')
	notifications = db.relationship('Notification', backref='user',lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def avatar(self, size):
		digest= md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
	def follow(self, user):
		if not self.is_following(user):
			self.followed.append(user)
	def unfollow(self, user):
		if self.is_following(user):
			self.followed.remove(user)
	def is_following(self, user):
		return self.followed.filter(followers.c.followed_id == user.id).count() > 0
	def followed_posts(self):
		followed = Post.query.join(followers,(followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id)
		own = Post.query.filter_by(user_id=self.id)
		return followed.union(own).order_by(Post.timestamp.desc())
	def get_reset_password_token(self, expires_in=600):
		return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},current_app.config['SECRET_KEY'], algorithm='HS256')
	def new_messages(self):
		last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
		return Message.query.filter_by(recipient=self).filter(Message.timestamp > last_read_time).count()
	def add_notification(self, name, data):
		self.notifications.filter_by(name=name).delete()
		n = Notification(name=name, payload_json=json.dumps(data), user=self)
		db.session.add(n)
		return n
	@staticmethod
	def verify_reset_password_token(token):
		try:
			id = jwt.decode(token, current_app.config['SECRET_KEY'],algorithms=['HS256'])['reset_password']

		except:
			return
		return User.query.get(id)
@login.user_loader
def load_user(id):   
	return User.query.get(int(id))
        
                
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	pinned = db.Column(db.Boolean, default=False, )
	def __repr__(self):
		return '<Post {}>'.format(self.body)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)

    def get_data(self):
    	return json.loads(str(self.payload_json))