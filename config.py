import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'clemsonite'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAILGUN_KEY=os.environ.get('MAILGUN_KEY')
	MAILGUN_DOMAIN=os.environ.get('MAILGUN_DOMAIN')
	POSTS_PER_PAGE = 50
