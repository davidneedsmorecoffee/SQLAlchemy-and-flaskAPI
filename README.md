# SQLAlchemy and Python for data analysis

In this example
* **Part I** - Python and SQLAlchemy were used to do basic climate analysis and data exploration of climate database (see `hawaii.sqlite`; based on `hawaii-measurements.csv`, and `hawaii-stations`). 
* **Part II** - Flask API setup. Multiple routes were set up for different functions.

## Part I: Climate Analysis and Exploration

* All analyses described were performed using SQLAlchemy ORM queries, Pandas, and/or Matplotlib (see `exploratory climate analysis_DL_clean.ipynb`)

* Used SQLAlchemy `create_engine` to connect to sqlite database.

* Used SQLAlchemy `automap_base()` to reflect tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Ploted the results using the DataFrame `plot` method.

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Identify the station with the highest number of observations

* Designed a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.

  * Constructed a histogram

## Part II: Climate App using Flask API

* Designed a Flask API based on the queries described.
* Used Flask `jsonify` to convert API data into a valid JSON response object.

* Use FLASK to create your routes.

### Routes
#### The following routes were established:

* `/`

  * Home page.
  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

