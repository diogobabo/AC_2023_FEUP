import sqlite3
import pandas as pd
import numpy as np

# Specify your database path
db_path = 'data.db'

# Connect to the SQLite database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Read CSV files into pandas DataFrames
coaches_df = pd.read_csv('./Comp_Dataset/coaches.csv')
players_teams_df = pd.read_csv('./Comp_Dataset/players_teams.csv')
teams_df = pd.read_csv('./Comp_Dataset/teams.csv')

# Define default or not relevant values
default_coach_value = 'default_coach_value'
default_team_value = 'default_team_value'

# Insert new rows into the coaches table
for index, row in coaches_df.iterrows():
    values = (row.get('coachID', None),
              row.get('year', None),  # Use None for SQLite to handle as NULL
              row.get('tmID', None),
              row.get('lgID', None),
              row.get('stint', None))  # Use None for SQLite to handle as NULL
    query = f"INSERT INTO coaches (coachID, year, tmID, lgID, stint) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, values)

# Insert new rows into the players_teams table
for index, row in players_teams_df.iterrows():
    values = (row.get('playerID', None),  # Use None for SQLite to handle as NULL
              row.get('year', None),
              row.get('stint', None),
              row.get('tmID', None),
              row.get('lgID', None))
    query = f"INSERT INTO players_teams (playerID, year, stint, tmID, lgID) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, values)

# Insert new rows into the teams table
for index, row in teams_df.iterrows():
    values = (row.get('year', None),
              row.get('lgID', None),
              row.get('tmID', None),
              row.get('franchID', None),
              row.get('confID', None),
              row.get('name', None),
              row.get('arena', None))
    query = f"INSERT INTO teams (year, lgID, tmID, franchID, confID, name, arena) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, values)

# Commit the changes and close the connection
connection.commit()
connection.close()
