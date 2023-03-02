
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify

################################################
# Database Setup
#################################################
engine = create_engine("sqlite:////Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    """List all available API Routes"""
    return(
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end>'
    )

@app.route('/api/v1.0/precipitation<br/>')
def precipitation():
    #Open Python session to database
    session = Session(engine)

    #Query for 12 months of precipitation
    precipitation_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= last_year_date).all()
    #Create dictionary and add values from precipitation_data query
    date_list = []

    for date, prcp in precipitation_data:
        results_dict = {}
        new_dict[date] = prcp
        date_list.append(results_dict)

    session.close()

    #Return to api
    return jsonify(date_list)

@app.route('/api/v1.0/stations<br/>')
def stations():


@app.route('/api/v1.0/tobs<br/>')
def tobs():


@app.route('/api/v1.0/<start><br/>')
def start_temp_range():


@app.route('/api/v1.0/<start>/<end>')
def start_end_temp_range():