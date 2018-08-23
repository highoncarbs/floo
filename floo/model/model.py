from app import db
from flask_login import UserMixin

class User(UserMixin , db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50) , unique=True, nullable=False)
    password = db.Column(db.String(300 ), nullable=False)

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
    typeof = db.Column(db.String(20) , nullable = False)
    name =  db.Column(db.String(20) , nullable = False)
    depart = db.Column(db.String(20) , nullable = False)
    arrival = db.Column(db.String(20) , nullable = False)
    origin_id = db.Column(db.Integer , db.ForeignKey('airportorigin.id'))
    destination_id = db.Column(db.Integer , db.ForeignKey('airportdest.id'))
    time = db.Column(db.String(10) , nullable = False)
