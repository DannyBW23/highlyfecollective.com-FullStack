import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor  
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_message = ''
login.login_view= 'auth.login'
mail = Mail() 
ckeditor = CKEditor()
csrf = CSRFProtect()
bootstrap=Bootstrap()
moment = Moment()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)
	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)
	mail.init_app(app)
	csrf.init_app(app)
	ckeditor.init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)





	from app.errors import bp as errors_bp
	app.register_blueprint(errors_bp)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)


	if not app.debug and not app.testing:
		if not os.path.exists('logs'):
			os.mkdir('logs')
		file_handler = RotatingFileHandler('logs/Highlyfe.log', maxBytes=10240, backupCount=10)	
		file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
		file_handler.setLevel(logging.INFO)
		app.logger.addHandler(file_handler)
		app.logger.setLevel(logging.INFO)
		app.logger.info('Highlyfe startup')
	return app 


from app import models #errors, routes

