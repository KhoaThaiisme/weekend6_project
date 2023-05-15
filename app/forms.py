from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class MarvelForm(FlaskForm):
    name= StringField('name', validators=[DataRequired()])
    description= StringField('description', validators=[DataRequired()])
    comic_appeared_in= StringField('comic_appeared_in')
    super_powers = StringField('super_power', validators=[DataRequired()])
    submit= SubmitField('Add')