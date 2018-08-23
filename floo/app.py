from flask import Flask , render_template , request , redirect , session , abort , url_for , g , flash , jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql 
from flask_login import LoginManager , login_user  , login_required , logout_user , current_user 
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from model import forms , model

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/' ,  methods=['POST' , 'GET'])
@login_required
def index():
    form = forms.search_form()
    user = current_user.username 
    form.origin.choices = [ (r.id , r.city ) for r in model.Airportorigin.query.order_by('city') ]
    form.destination.choices = [ (r.id , r.city ) for r in model.Airportdest.query.order_by('city') ]

    if form.validate_on_submit():
        flights = db.session.query(model.flights).filter(model.flights.origin_id == int(form.origin.data)).filter(model.flights.destination_id == int(form.destination.data)).all()
        date = form.date.data
        person = form.num_people.data
        return render_template('list.html' , flights = flights , username = user , date = date,  person = person), 200
        
    return render_template('index.html' , form=  form , username = user), 200


@app.route('/flights/<f_id>' , methods=['POST' , 'GET'])
@login_required
def flights(f_id):
    user = current_user
    book = model.Book(flight_id = f_id , user_id = user.id)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('user'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    """
    form = forms.loginform()
    mssg = ""

    if form.validate_on_submit():
        user = model.User.query.filter_by(username=form.username.data).first()
        print(user)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                print("loggedin")
                return redirect(url_for('index'))
            else:
                mssg = "Invalid Username or Password"
                return render_template('login.html', subtitle="Login", formlogin =form, error_mssg=mssg)
        else:
            return render_template('login.html', subtitle="Login", formlogin =form, error_mssg="No such account exists")

    print(form.errors)
    return render_template('login.html', subtitle="Login", formlogin = form, error_mssg=mssg), 200


@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    form = forms.signupform()
    mssg = ""
    if form.validate_on_submit():
        
        user = model.User.query.filter_by(username = form.username.data).first()
        
        if user is None:
        
            hashed_pass = generate_password_hash(form.password.data , method='sha256')
            new_user = model.User(username = form.username.data , password = hashed_pass)
    
            db.session.add(new_user)
            db.session.commit()
            db.session.close()
            return redirect(url_for('login'))
        

        else:
            return render_template('signup.html' , formsign = form ,subtitle = "Signup" ,error_mssg = "Email already exists.")

        db.session.close()

    return render_template('signup.html' , subtitle = "Signup" , formsign = form , error_mssg = mssg),200

@app.route('/forgot' , methods=['GET', 'POST'])
def forgot():
    return render_template('login.html' , subtitle = "Forgot"),200


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return model.User.query.get(int(user_id))

@app.route('/user' , methods=['GET' , 'POST'])
@login_required
def user():
    '''
        User setup done here
        - Username
        - Email for sending
        - Delete Account
        - Reset data
        - Export data 
    '''
    user = current_user.username 
    booking = db.session.query(model.User).filter( model.User.id == user.id).all()
    return render_template('user.html' ,username=user),200
