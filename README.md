# NBA-Stats-data

NBA League Leaders Data Processing
This repository contains a Python script that fetches NBA league leader statistics using the nba_api package, processes the data with pandas, and stores it in a SQL Server database using SQLAlchemy and pyodbc. Additionally, the script creates a SQL view to easily query specific subsets of the data.

Requirements
To run this script, you need the following Python libraries installed:

pandas
sqlalchemy
pyodbc
nba_api
You can install these dependencies using pip:
pip install pandas sqlalchemy pyodbc nba_api

Database Setup
Ensure you have access to a SQL Server instance where you can create a database. Update the server and database variables in the script to match your SQL Server's configuration.

Script Overview
Fetch NBA Data: Uses nba_api to get current NBA league leaders data.
Export to CSV (optional): The script includes a line (currently commented out) to save the data to a CSV file.
Connect to SQL Server: Uses SQLAlchemy and pyodbc to connect to a SQL Server database.
Save Data to SQL Table: Loads the NBA data into a table named NBA_STATS_2024.
Create SQL View: Creates a SQL view named NBA_VIEW_2024_PYTHON to simplify querying specific columns.
Usage

Notes
Make sure the SQL Server instance is accessible and the necessary ODBC driver is installed (ODBC Driver 17 for SQL Server).
The script replaces the existing table (NBA_STATS_2024) if it already exists. Adjust if_exists parameter in df.to_sql() if you want to append or fail instead.
Review the view creation SQL to ensure it meets your data requirements.
