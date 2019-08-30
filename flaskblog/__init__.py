import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import stripe

stripe_keys = {
  'secret_key': 'sk_test_t0yFEaPdbVUsjB9hzb2ZRsGj',
  'publishable_key': 'pk_test_cPNvqfSAK8oSRiFIesZWr3xN'
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.config['SECRET_KEY'] = '157f55b29f7ef3f46937364a273e5ea0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
'''
    Set a category for how to display the information
    if you try to access page that requires you to login
'''
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'admin@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'

#You can use the following lines instead if
# you've set you password and email as environ vars
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

mail = Mail(app)

from flaskblog import routes
