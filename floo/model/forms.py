from wtforms import StringField, BooleanField , DateField , PasswordField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length , DataRequired ,Regexp , Optional
from flask_wtf import FlaskForm 

class search_form(FlaskForm):
    origin = StringField('origin' , validators=[InputRequired()])
    destination = StringField('destination' , validators=[InputRequired()])
    date = DateField()
    num_people = StringField('num_people' , validators=[InputRequired()])

class loginform(FlaskForm):
    username = StringField('username' , validators=[InputRequired()])
    password = PasswordField('password' , validators=[InputRequired()])
    
class signupform(FlaskForm):
    username = StringField('username' , validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    
    
