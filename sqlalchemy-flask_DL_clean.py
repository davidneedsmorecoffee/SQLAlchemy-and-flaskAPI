import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# Create the inspector and connect it to the engine
inspector = inspect(engine)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
#### Passenger = Base.classes.passenger

Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# /
# Home page.
# List all routes that are available.
@app.route("/")
def welcome():
    """List all available api routes."""

    return (
        """Available Routes:<br/>"""
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/><br/>"
        f"for 'start' and 'end' portion of the URL, enter date in the following format: <br>"
        f"yyyy-mm-dd"
    )

# Create our session (link) from Python to the DB
#session = Session(engine)


# /api/v1.0/precipitation
# Convert the query results to a Dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    ## instruction didn't specify what the query is.  Use start date of 2017-07-07 as the query
    query_result = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2017-07-07').\
    order_by(Measurement.date).all()
    session.close()

    precipitation_values_list = []
    # go through the query_results, grab the date and prcp, put it into dictionary as key and value
    # append dictionary to the list 
    for i in query_result:
        precipiation_dictionary = {"Date":i.date, "Prcp": i.prcp}
        precipitation_values_list.append(precipiation_dictionary)
    # Convert list of tuples into normal list
    result = list(np.ravel(precipitation_values_list))
    return jsonify(result)
 


# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    query_result = session.query(Station.station).all()
    session.close()
    # Convert list of tuples into normal list
    result = list(np.ravel(query_result))
    # jsonify the list
    return jsonify(result)


# /api/v1.0/tobs
# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    query_result = session.query(Measurement.tobs).all()
    session.close()
    # Convert list of tuples into normal list
    result = list(np.ravel(query_result))
    # jsonify the list
    return jsonify(result)


# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
@app.route("/api/v1.0/<start>")
def query_start_only(start):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    query_result = session.query(*sel).\
        filter(Measurement.date >= start).all()
    session.close()

    result = list(np.ravel(query_result))
    return jsonify(result)

# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
@app.route("/api/v1.0/<start>/<end>")
def query_start_end(start, end):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    query_result = session.query(*sel).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
 
    result = list(np.ravel(query_result))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
