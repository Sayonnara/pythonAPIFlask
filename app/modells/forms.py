from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("username", validators=[DataRequired()])
    password = PassowrdField(" password",  validators=[DataRequired()])
    remenber_me = BooleanField("remenber_me")
