from app import app , db
import sys
from testdata import flightdata , airportdata

if __name__ == "__main__":
        db.create_all()
        app.run(debug=True)