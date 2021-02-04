"""
Put your forms here
WTForms is a flexible forms validation
and rendering library for Python web development.
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
# from wtforms.fields.html5 import DateField, TimeField, DateTimeField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password',
                             validators=[InputRequired(),
                                         Length(min=8, max=80)])


class RegisterForm(FlaskForm):
    username = StringField('username',
                           validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password',
                             validators=[InputRequired(),
                                         Length(min=8, max=80)])
    email = StringField('email',
                        validators=[InputRequired(), Email()])
