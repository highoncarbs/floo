from app import db
from model import model

def airportdata():
    add_airdata('DEL' , 'DELHI')
    add_airdata('JAI' , 'JAIPUR')
    add_airdata('BLR' , 'BENGALURU')
    add_airdata('CCU' , 'KOLKATA')
    add_airdata('BKK' , 'BANGKOK')

    db.session.commit()
    db.session.close()


def add_airdata( pre_name , city ):
    data = model.Airportorigin(pre_name = pre_name , city = city)
    ndata = model.Airportdest(pre_name = pre_name , city = city)

    db.session.add(data)
    db.session.add(ndata)

if __name__ == "__main__":
    airportdata()