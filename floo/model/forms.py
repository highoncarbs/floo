from wtforms import StringField, BooleanField , DateField , PasswordField
from wtforms.widgets import Input
from wtforms.validators import InputRequired, Length , DataRequired ,Regexp , Optional
from wtforms_alchemy.fields import SelectField
from flask_wtf import FlaskForm 


class search_form(FlaskForm):
    origin = SelectField('origin' ,validators=[InputRequired()], coerce = int )
    destination = SelectField('destination',validators=[InputRequired()],coerce = int)
    date = StringField('date')
    num_people = StringField('num_people' )

class loginform(FlaskForm):
    username = StringField('username' , validators=[InputRequired()])
    password = PasswordField('password' , validators=[InputRequired()])
    
class signupform(FlaskForm):
    username = StringField('username' , validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    
    
