# Module 9.4.3 - setting up Flask routes
# Module 9.5.x - creating the Flask Weather App
# import core modules
import datetime as dt
import numpy as np
import pandas as pd

# now SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# now import flask, jsonify
from flask import Flask, jsonify

# setup DB engine, base classes, and session
"""
engine = create_engine("sqlite:///hawaii.sqlite")
  this kept getting this error:
  sqlalchemy.exc.ProgrammingError: (sqlite3.ProgrammingError) SQLite objects created in a
   thread can only be used in that same thread. The object was created in 
   thread id ####1 and this is thread id ####2.
after poking around found this stackoverflow item and tried the connection parameter below
  -- it works :) 
https://stackoverflow.com/questions/34009296/using-sqlalchemy-session-from-flask-raises-sqlite-objects-created-in-a-thread-c

"""

engine = create_engine('sqlite:///hawaii.sqlite?check_same_thread=False')

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# Create a new Flask instance
app = Flask(__name__)

 # create the welcome (root) route
@app.route('/')
def welcome():
    return(
    """
    Welcome to the Climate Analysis API!
    Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
    """
    )

# create the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# create the stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# create the monthy temperature route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create the stats route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)