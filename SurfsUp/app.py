# Import the dependencies.
# import datetime as dt
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
    )


# @app.route("/api/v1.0/precipitation")
# def precipitations():
 
#    session = Session(engine)
#    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date).all()
#    result_dict = dict(results)
#    session.close()
   
#    return jsonify(result_dict)

# @app.route("/api/v1.0/stations")
# def stations():

#     session = Session(engine)
#     stations = session.query(Measurement.station, func.count(Measurement.id)).group_by(Measurement.station).\
#         order_by(func.count(Measurement.id).desc()).all()

#     stations_dict = dict(stations)
#     session.close()

#     return jsonify(stations_dict)

# @app.route("/api/v1.0/tobs")
# def tobs():
#     session = Session(engine)

#     max_temp_observed = session.query(Measurement.station, Measurement.station).filter(Measurement.date >= '2016-08-23').all()

#     tobs_dict = dict(max_temp_observed)

#     session.close()

#     return jsonify(tobs_dict)

# @app.route("/api/v1.0/<start><br/>")
# def start(start):
#     session = Session(engine)

#     results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), 
#         func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date >= start).all()

#     session.close()

if __name__ == '__main__':
    app.run()

