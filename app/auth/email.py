from flask import render_template, current_app
import requests
def send_password_reset_email(to_address, from_address, subject, plaintext, html):
	r = requests.post("https://api.mailgun.net/v2/%s/messages" % current_app.config['MAILGUN_DOMAIN'],auth=("api", current_app.config['MAILGUN_KEY']),data={"from": from_address, "to": to_address, "subject": subject,"text": plaintext, "html": html})
	return r
 

def send_mail(user):
    token = user.get_reset_password_token()
    send_password_reset_email('[Highlyfe] Reset Your Password',sender=current_app.config['MAIL_USERNAME'],recipients=[user.email],text_body=render_template('email/reset_password.txt',user=user, token=token),html_body=render_template('email/reset_password.html',user=user, token=token))
 
 # from app.email import send_email 
# send_email('[Highlyfe] Reset Your Password',sender=current_app.config['MAIL_USERNAME'],recipients=[user.email],text_body=render_template('email/reset_password.txt',user=user, token=token),html_body=render_template('email/reset_password.html',user=user, token=token))


