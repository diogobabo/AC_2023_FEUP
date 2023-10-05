import pandas as pd
import sqlite3

query = """
    SELECT
        t.year, t.tmID, t.playoff,
        pt.GP, pt.GS, pt.minutes, pt.points, pt.oRebounds, pt.dRebounds, pt.assists,
        s.round, s.tmIDWinner, s.tmIDLoser, s.W, s.L,
        tp.W AS post_W, tp.L AS post_L,
        ap.award,
        t.o_fgm, t.o_fga, t.o_ftm, t.o_fta, t.o_3pm, t.o_3pa, t.o_oreb, t.o_dreb, t.o_reb,
        t.o_asts, t.o_pf, t.o_stl, t.o_to, t.o_blk, t.o_pts, t.d_fgm, t.d_fga, t.d_ftm, t.d_fta,
        t.d_3pm, t.d_3pa, t.d_oreb, t.d_dreb, t.d_reb, t.d_asts, t.d_pf, t.d_stl, t.d_to, t.d_blk, t.d_pts,
        p.GP AS player_GP, p.GS AS player_GS, p.minutes AS player_minutes,
        p.points AS player_points, p.oRebounds AS player_oRebounds, p.dRebounds AS player_dRebounds,
        p.assists AS player_assists
    FROM teams AS t
    JOIN players_teams AS pt ON t.year = pt.year AND t.tmID = pt.tmID
    JOIN series_post AS s ON t.year = s.year AND t.tmID = s.tmIDWinner
    JOIN teams_post AS tp ON t.year = tp.year AND t.tmID = tp.tmID
    LEFT JOIN awards_players AS ap ON t.year = ap.year AND pt.playerID = ap.playerID
    LEFT JOIN players_teams AS p ON t.year = p.year AND t.tmID = p.tmID
"""



db_path = 'data.db'
conn = sqlite3.connect(db_path)
data = conn.execute(query).fetchall()
conn.close()

df = pd.DataFrame(data, columns=[
    'year', 'tmID', 'playoff',
    'GP', 'GS', 'minutes', 'points', 'oRebounds', 'dRebounds', 'assists',
    'round', 'tmIDWinner', 'tmIDLoser', 'W', 'L', 'post_W', 'post_L', 'award',
    'o_fgm', 'o_fga', 'o_ftm', 'o_fta', 'o_3pm', 'o_3pa', 'o_oreb', 'o_dreb', 'o_reb',
    'o_asts', 'o_pf', 'o_stl', 'o_to', 'o_blk', 'o_pts',
    'd_fgm', 'd_fga', 'd_ftm', 'd_fta', 'd_3pm', 'd_3pa', 'd_oreb', 'd_dreb', 'd_reb',
    'd_asts', 'd_pf', 'd_stl', 'd_to', 'd_blk', 'd_pts',
    'GP', 'GS', 'minutes', 'points', 'oRebounds', 'dRebounds', 'assists'
])

df.to_csv('data.csv', index=False)

teams_df = pd.read_csv('teams.csv')
players_df = pd.read_csv('players.csv')
players_teams_df = pd.read_csv('players_teams.csv')

merged_df = teams_df.merge(players_teams_df, on=['year', 'tmID'], how='inner')

# Aggregate player statistics by team and year
agg_df = merged_df.groupby(['year', 'tmID']).agg({
    'points': 'sum',
    'rebounds': 'sum',
    'assists': 'sum',
    # Add other player-level statistics as needed
}).reset_index()

#print data to csv data is the result of a query

