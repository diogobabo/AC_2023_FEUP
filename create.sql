CREATE TABLE teams(
					  year INTEGER,
					  lgID VARCHAR(255),
					  tmID VARCHAR(255),
					  franchID VARCHAR(255),
					  confID VARCHAR(255),
					  divID VARCHAR(255),
					  rank INTEGER,
					  playoff VARCHAR(255),
					  seeded INTEGER,
					  firstRound VARCHAR(255),
					  semis VARCHAR(255),
					  finals VARCHAR(255),
					  name VARCHAR(255),
					  o_fgm INTEGER,
					  o_fga INTEGER,
					  o_ftm INTEGER,
					  o_fta INTEGER,
					  o_3pm INTEGER,
					  o_3pa INTEGER,
					  o_oreb INTEGER,
					  o_dreb INTEGER,
					  o_reb INTEGER,
					  o_asts INTEGER,
					  o_pf INTEGER,
					  o_stl INTEGER,
					  o_to INTEGER,
					  o_blk INTEGER,
					  o_pts INTEGER,
					  d_fgm INTEGER,
					  d_fga INTEGER,
					  d_ftm INTEGER,
					  d_fta INTEGER,
					  d_3pm INTEGER,
					  d_3pa INTEGER,
					  d_oreb INTEGER,
					  d_dreb INTEGER,
					  d_reb INTEGER,
					  d_asts INTEGER,
					  d_pf INTEGER,
					  d_stl INTEGER,
					  d_to INTEGER,
					  d_blk INTEGER,
					  d_pts INTEGER,
					  tmORB INTEGER,
					  tmDRB INTEGER,
					  tmTRB INTEGER,
					  opptmORB INTEGER,
					  opptmDRB INTEGER,
					  opptmTRB INTEGER,
					  won INTEGER,
					  lost INTEGER,
					  GP INTEGER,
					  homeW INTEGER,
					  homeL INTEGER,
					  awayW INTEGER,
					  awayL INTEGER,
					  confW INTEGER,
					  confL INTEGER,
					  min INTEGER,
					  attend INTEGER,
					  arena VARCHAR(255),
					  CONSTRAINT PK_TEAMS PRIMARY KEY (year, tmID)
);

CREATE TABLE coaches(
    coachID VARCHAR(255),
    year INTEGER,
    tmID VARCHAR(255),
    lgID VARCHAR(255),
    stint INTEGER,
    won INTEGER,
    lost INTEGER,
    post_wins INTEGER,
    post_losses INTEGER,

    CONSTRAINT FOREIGNKEY_year FOREIGN KEY (year) REFERENCES teams(year) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FOREIGNKEY_tmID FOREIGN KEY (tmID) REFERENCES teams(tmID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT PK_coaches PRIMARY KEY (coachID, stint, year, tmID)
);

CREATE TABLE players(
    bioId VARCHAR(255) PRIMARY KEY,
    pos VARCHAR(255),
    firstseason INTEGER,
    lastseason INTEGER,
    height REAL,
    weight INTEGER,
    college VARCHAR(255),
    collegeOther VARCHAR(255),
    birthDate VARCHAR(255),
    deathDate VARCHAR(255)
);



create table series_post(
					year INTEGER,
					round VARCHAR(255), 
					series VARCHAR(255), 
					tmIDWinner VARCHAR(255),
					lgIDWinner VARCHAR(255),
					tmIDLoser VARCHAR(255),
					lgIDLoser VARCHAR(255),
					W INTEGER,
					L INTEGER,

					CONSTRAINT FOREIGNKEY_year FOREIGN KEY (year) REFERENCES teams(year) ON DELETE CASCADE ON UPDATE CASCADE
);

create table players_teams(
					playerID VARCHAR(255),
					year INTEGER, 
					stint INTEGER, 
					tmID VARCHAR(255),
					lgID VARCHAR(255),
					GP INTEGER,
					GS INTEGER,
					minutes INTEGER,
					points INTEGER,
					oRebounds INTEGER,
					dRebounds INTEGER,
					rebounds INTEGER,
					assists INTEGER,
					steals INTEGER,
					blocks INTEGER,
					turnovers INTEGER,
					PF INTEGER,
					fgAttempted INTEGER,
					fgMade INTEGER,
					ftAttempted INTEGER,
					ftMade INTEGER,
					threeAttempted INTEGER,
					threeMade INTEGER,
					dq INTEGER,
					PostGP INTEGER,
					PostGS INTEGER,
					PostMinutes INTEGER,
					PostPoints INTEGER,
					PostoRebounds INTEGER,
					PostdRebounds INTEGER,
					PostRebounds INTEGER,
					PostAssists INTEGER,
					PostSteals INTEGER,
					PostBlocks INTEGER,
					PostTurnovers INTEGER,
					PostPF INTEGER,
					PostfgAttempted INTEGER,
					PostfgMade INTEGER,
					PostftAttempted INTEGER,
					PostftMade INTEGER,
					PostthreeAttempted INTEGER,
					PostthreeMade INTEGER,
					PostDQ INTEGER,


					CONSTRAINT FOREIGNKEY_year FOREIGN KEY (year) REFERENCES teams(year) ON DELETE CASCADE ON UPDATE CASCADE,
					CONSTRAINT FOREIGNKEY_playerID FOREIGN KEY (playerID) REFERENCES players(bioID) ON DELETE CASCADE ON UPDATE CASCADE,
					CONSTRAINT FOREIGNKEY_tmID FOREIGN KEY (tmID) REFERENCES teams(tmID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE teams_post(
    year INTEGER,
    tmID VARCHAR(255),
    lgID VARCHAR(255),
    W INTEGER,
    L INTEGER,

    CONSTRAINT FOREIGNKEY_year FOREIGN KEY (year) REFERENCES teams(year) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FOREIGNKEY_tmID FOREIGN KEY (tmID) REFERENCES teams(tmID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE awards_players(
    playerID VARCHAR(255),
    award VARCHAR(255),
    year INTEGER,
    lgID VARCHAR(255),

    CONSTRAINT FOREIGNKEY_playerID FOREIGN KEY (playerID) REFERENCES players(bioId) ON DELETE CASCADE ON UPDATE CASCADE
);





