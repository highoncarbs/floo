from app import db
from flask_login import UserMixin

class User(UserMixin , db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50) , unique=True, nullable=False)
    password = db.Column(db.String(300 ), nullable=False)
    flights = db.relationship('Booking' , backref="flights" , lazy= "dynamic")
   
    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Airportorigin(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    pre_name = db.Column(db.String(5) , unique=True , nullable = False)
    city = db.Column(db.String(20) , unique = True , nullable = False)
    flight_or = db.relationship('flights' , backref="origin" , lazy= "dynamic")

class Airportdest(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    pre_name = db.Column(db.String(5) , unique=True , nullable = False)
    city = db.Column(db.String(20) , unique = True , nullable = False)
    flight_dt = db.relationship('flights' , backref="destination" , lazy= "dynamic")

class flights(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    img = db.Column(db.String(50) , nullable=False)
    typeof = db.Column(db.String(30) , nullable = False)
    name =  db.Column(db.String(20) ,unique=True , nullable = False)
    depart = db.Column(db.String(20) , nullable = False)
    arrival = db.Column(db.String(20) , nullable = False)
    origin_id = db.Column(db.Integer , db.ForeignKey('airportorigin.id'))
    destination_id = db.Column(db.Integer , db.ForeignKey('airportdest.id'))
    fare = db.Column(db.String(10) , nullable = False)
    time = db.Column(db.String(10) , nullable = False)
    booking = db.relationship('Booking' , backref="booking" , lazy ="dynamic")

class Booking(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    flight_id = db.Column(db.Integer , db.ForeignKey('flights.id'))
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    date = db.Column(db.String(10) , nullable = False)
    people = db.Column(db.String(10) , nullable=False)