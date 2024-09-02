import pandas as pd
import sqlalchemy
from sqlalchemy.sql import text
import pyodbc
from nba_api.stats.endpoints import leagueleaders


league_leaders = leagueleaders.LeagueLeaders()
df = league_leaders.get_data_frames()[0]
###CSV FILE ###
#df.to_csv('C:\\Users\\naime\\Downloads\\nba_league_leaders.csv', index=False)

server = 'DESKTOP-CGM6H41'
database = 'NBA_STATS'
connection_string = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

engine = sqlalchemy.create_engine(connection_string)

df.to_sql("NBA_STATS_2024", engine, if_exists="replace")

####ATTEMPT###
create_view_query = """
CREATE VIEW NBA_VIEW_2024_PYTHON AS
SELECT 
    PLAYER,
    GP,
    PTS,
    AST,
    REB,
    DREB,
    OREB,
    STL,
    BLK,
    TOV,
    FGA,
    FGM,
    FG_PCT,
    FG3_PCT,
    FT_PCT,
    MIN,
    TEAM
FROM NBA_STATS_2024
"""

with engine.connect() as connection:
    connection.execute(text(create_view_query))
####ATTEMPT###
print("Table Created")
