# surfs_up

## Project Overview
An investor wishes to know about the viability of starting a surfing-based business in Hawaii. The climate data for the area is analyzed using SQLAlchemy to access the data stored in a SQLite database.

## Resources

### Data Sources

- climate_analysis.ipynb
- hawaii.sqlite

### Software

- Python 3 Environment (Notebook Files):

    1. Python 3.9.13
    2. Jupyter Notebook 6.4.12
    3. Pandas 1.4.4
    4. NumPy 1.21.5
    5. Matplotlib 3.5.1
    6. SQLAlchemy 1.4.39

- PythonData Environment (Flask app):

    1. Python 3.7.13
    2. Visual Studio Code 1.71.2
    3. Pandas 1.3.5
    4. NumPy 1.21.5
    5. SQLAlchemy 1.4.32
    6. Flask 1.1.2

## Data Analysis Process

### Handling SQLAlchemy
The data is stored in a SQLite file, so SQLAlchemy is used to access and analyze. The `climate_analysis` program creates an engine to prepare and connect to the database, and reflects the database into a new model for work. The tables in the database are saved into references (for simpler access), and a session is established to link Python to the database.

The initialization completed, some queries were made, some results were saved into DataFrames, and those DataFrames to make a few plots.

### Preparing a Flask Application
The `app` Python file holds the script for the Flask application. The first part of the script imports all the necessary dependencies, prepares the SQLite database with SQLAlchemy, and initializes the Flask app.

After initialization, five routes were established:

1. The first route is always the root and serves to introduce the user to the app and to explain what the other routes are. These routes are appended to the URL of the root in order to access them.

2. The second route is the `precipitation` route. It uses the active SQLAlchemy session to query the Measurement table and get the measured precipitation data between August 23, 2016 and August 23, 2017. The results are returned to the user as a JSON object.

3. The third route is the `stations` route. It uses the active SQLAlchemy session to query the Station table and get a list of the stations in use. The list is returned to the user as a JSON object.

4. The fourth route is the `tobs` route. It uses the active SQLAlchemy session to query the Measurement table and get a list of the temperatures observed by Station USC00519281 between August 23, 2016 and August 23, 2017. The list is returned to the user as a JSON object.

5. The fifth route is the `temp` route. Unlike the other route, it requires the user to input at least a starting date and allows the user to optionally input an ending date. The active SQLAlchemy session uses the input to query the Measurement table and get the minimum observed temperature, the maximum observed temperature, and the average observed temperature for the designated date range. The start date is required and the end date is optional; without an end date, the query just runs from the start date to the last point in the table. However, the code is not necessarily robust; if the user inputs invalid date(s), then the program will not work properly. Invalid dates can involve the dates not following the proper format (YYYY-MM-DD), the dates not being within the range set in the table, the end date being earlier than the start date, or just no date at all.