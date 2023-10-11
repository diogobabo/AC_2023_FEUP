import pandas as pd
import sqlite3


players_df = pd.read_csv('Dataset/players.csv')

#remove column with only one value
players_df = players_df.drop(columns='lastseason', axis=1)

# Calculate the mean of non-zero heights
mean_height = players_df[players_df['height'] != 0]['height'].mean()

# Replace 0 with the mean height
players_df['height'] = players_df['height'].replace(0, mean_height)

# Calculate the mean of non-zero weights
mean_weight = players_df[players_df['weight'] != 0]['weight'].mean()

# Replace 0 with the mean weight
players_df['weight'] = players_df['weight'].replace(0, mean_weight)

# Delete the players that have died before the Year 1 (2000 ou 2001)

# Replace '0000-00-00' with pd.NaT (Not a Time)
players_df['deathDate'] = players_df['deathDate'].replace('0000-00-00', pd.NaT)

# Convert the 'deathDate' column to datetime format
players_df['deathDate'] = pd.to_datetime(players_df['deathDate'])

# Filter out rows where the death date is before the year 2000
players_df = players_df[(players_df['deathDate'].isna()) | (players_df['deathDate'].dt.year >= 2000)]


# Save the modified DataFrame to a CSV file
players_df.to_csv('modified_players.csv', index=False)


#------------------------- teams

teams = pd.read_csv('Dataset/teams.csv')

teams = teams.drop(columns=['seeded'], axis=1)



