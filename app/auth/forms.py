from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validate_on_submit import Required, Length, Email

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('keep me loged in')
    submit = SubmitField('Login In')
    
