from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	openid = StringField('openid' , validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)

class RegisterForm(FlaskForm):
	email = StringField('Email' ,validators=[DataRequired()])
	password = PasswordField('Email' ,validators=[DataRequired()])
	username = StringField('username' ,validators=[DataRequired()])