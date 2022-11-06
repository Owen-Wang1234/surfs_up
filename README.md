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

### Taking Temperatures for June and December
Two more queries are made for the Measurement table, both collect all the temperatures for a specific month (one for June, the other for December). Since only one column was selected, the results are converted into lists before they are stored into DataFrames for summarization, and index setting was not necessary.

## Discussion of June and December Temperatures
The summaries of the temperatures for the months of June and December in the database are tabulated as follows:

![Summaries of June and December Temps](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/Jun_Dec_Temps.png)

- The average temperature is about 74.94 &deg;F for June and about 71.04 &deg;F for December. Surprisingly, the temperature is only slightly cooler for December than for June but still above 70 &deg;F.

- The median temperature is 75 &deg;F for June and 71 &deg;F for December. The average values are very close to the median values, so the outliers are either non-consequential or non-existent.

- The month of June is 64 &deg;F at the coolest and 85 &deg;F at the warmest. The month of December is 56 &deg;F at the coolest and 83 &deg;F at the warmest. The maximum temperature is not too far apart, but the minimum temperature shows a much more stark difference of 8 degrees.

- Interestingly, the number of data points for June and December are not equal. This is because the database started at the beginning of 2010 but ended at August 2017, so December 2017 was not included.

## Summary
The temperature data are charted in box-and-whisker plots for easier visualization. The plots show that most of the observed temperatures (non-outliers) for both months are between 67 &deg;F and 80 &deg;F in general.

![Temperature Box-and-Whiskers](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/BoxPlots.png)

The temperatures appear relatively consistent, so the conditions seem ideal for opening a surfing and ice cream business. Further analysis can help answer any possible questions. Before doing so, a re-examination of all nine stations used to log the weather reveals something interesting: Two of them (USC00518838 and USC00516128) are not located anywhere near a beach, which could be confirmed by the elevation being in the triple digits (implying that these stations may be sitting on a mountainside). If any additional queries are to be carried out for this business, it might be helpful to exclude these two to obtain a more coast-centric weather analysis. For convenience of reference, the queries and additional action scripts used have been appended after the end of the Module Challenge Notebook file.

1. One additional query gathers the minimum, average, and maximum temperature over time grouped by year and month. The query filter excludes the two stations on the mountain. The results are placed into a Pandas DataFrame, which can then be exported into a CSV file or be plotted and manipulated as desired. As examples, some box plots are drawn up:

![Temperature Statistics](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/TempStats.png)

![Average Precipitation](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/AvgPrcp.png)

![Maximum Precipitation](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/MaxPrcp.png)

It appears that about 75% of the monthly minimum temperatures are above 60 &deg;F from looking at the first quartile line, and the minimum monthly average temperature lines up with the third quartile of the monthly minimum temperatures. No outliers are observed among the monthly temperature data.

The monthly average precipitation statistically should not exceed 0.3 inches (the four months that do are marked as outliers), and the monthly maximum precipitation statistically should not exceed 6 inches (the five months that do are marked as outliers).

Based on temperature and precipitation in the whole database, the conditions likely appear great for non-winter periods.

2. Another additional query aggregates the average temperature and precipitation for each coastal station by month (excluding the two mountain stations). The results are placed into a Pandas DataFrame to allow export into a CSV file or any desired future work. A pair of line charts are drawn up as an example of tracking the monthy average temperature and precipitation for each coastal station:

![Monthly Average Temp by Station](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/StationTemp.png)

![Monthly Average Prcp by Station](http://github.com/Owen-Wang1234/surfs_up/blob/main/Figures/StationPrcp.png)

As shown, the winter and early spring range (January, February, March, and December) may not be ideal based on average temperature, but the average precipitation lines can only point out that two stations report the highest precipitation averages almost consistently: USC00519281 and USC00513117. One interesting observation is that the average temperature curves show a noticible split between two groups; one group always have higher average temperatures than the other group from April to October. It would appear that there are four areas that may be ideal:

| Station | Area |
| --- | --- |
| USC00514830 | Kualoa Ranch |
| USC00517948 | Pearl City |
| USC00519397 | Waikiki |
| USC00519523 | Waimanalo |