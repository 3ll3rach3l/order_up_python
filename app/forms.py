from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import (StringField, SubmitField, PasswordField)

class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")
