from app import db , url_for
from model import model

def airportdata():
    add_airdata('DEL' , 'DELHI')
    add_airdata('JAI' , 'JAIPUR')
    add_airdata('BLR' , 'BENGALURU')
    add_airdata('CCU' , 'KOLKATA')

    db.session.commit()
    db.session.close()

def flightdata():
    ben_o = db.session.query(model.Airportorigin).filter(model.Airportorigin.pre_name == 'BLR').first()
    ben_d = db.session.query(model.Airportdest).filter(model.Airportdest.pre_name == 'BLR').first()

    jai_o = db.session.query(model.Airportorigin).filter(model.Airportorigin.pre_name == 'JAI').first()
    jai_d = db.session.query(model.Airportdest).filter(model.Airportdest.pre_name == 'JAI').first()

    
    del_o = db.session.query(model.Airportorigin).filter(model.Airportorigin.pre_name == 'DEL').first()
    del_d = db.session.query(model.Airportdest).filter(model.Airportdest.pre_name == 'DEL').first()

    ccu_o = db.session.query(model.Airportorigin).filter(model.Airportorigin.pre_name == 'CCU').first()
    ccu_d = db.session.query(model.Airportdest).filter(model.Airportdest.pre_name == 'CCU').first()

    add_flightdata('indigo' , 'Non-Stop' , 'IN-727', '08:00' , '10:00' , '2', del_o.id , ben_d.id , '5000' )
    add_flightdata('airasia' , 'Non-Stop' , 'AA-707', '09:00' , '11:00' , '2' ,del_o.id , ben_d.id , '4500')
    add_flightdata('emirates' , 'Non-Stop' , 'E-A320', '05:00' , '06:30' , '1:30', del_o.id , jai_d.id , '7000')
    add_flightdata('emirates' , '1 stop - DEL - 2 Hours' , 'E-A342', '05:00' , '10:00','5' , del_o.id , ben_d.id ,'12000' )
    add_flightdata('indigo' , 'Non-Stop' , 'IN-701', '13:00' , '15:00' ,'2' , ccu_o.id , jai_d.id , '4700')

    db.session.close()

def add_airdata( pre_name , city ):
    data = model.Airportorigin(pre_name = pre_name , city = city)
    ndata = model.Airportdest(pre_name = pre_name , city = city)

    db.session.add(data)
    db.session.add(ndata)

def add_flightdata(air , typeof , name , depart , arrival , time , origin_id , dest_id , fare):
    if air is 'indigo':
        data = model.flights(img = "./static/images/indigo.jpg" , typeof= typeof , name= name , depart= depart ,
            arrival= arrival , time= time , origin_id = origin_id , destination_id = dest_id , fare = fare)
        db.session.add(data)
        db.session.commit()

    elif air is 'airasia':
        adata = model.flights(img ="./static/images/airasia.jpg" ,typeof= typeof , name= name , depart= depart ,
            arrival= arrival , time= time , origin_id = origin_id , destination_id = dest_id , fare = fare)
        db.session.add(adata)
        db.session.commit()
    elif air is 'emirates':
        edata = model.flights(img ="./static/images/emirates.jpg" , typeof= typeof , name= name , depart= depart ,
            arrival= arrival , time= time , origin_id = origin_id , destination_id = dest_id , fare = fare)
        db.session.add(edata)
        db.session.commit()
    
