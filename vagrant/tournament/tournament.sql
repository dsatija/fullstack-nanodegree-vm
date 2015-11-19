-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Connect to Database
  DROP DATABASE IF EXISTS tournament;
  CREATE DATABASE tournament;
  \c tournament

--Drop view if exists

  DROP VIEW IF EXISTS WINS CASCADE;
  DROP VIEW IF EXISTS TOTAL_MATCHES CASCADE ;
  DROP VIEW IF EXISTS PLAYER_STANDINGS CASCADE;

--Drop old tables

  DROP TABLE IF EXISTS Matches CASCADE ;
  DROP TABLE IF EXISTS Players CASCADE ;


--Create table for player details
  CREATE TABLE Players (
	id SERIAL primary key,
	player_name varchar(255) NOT NULL
  );

--Create Matches Table
  CREATE TABLE Matches (
 	id SERIAL primary key,
 	player int references Players(id) ON DELETE CASCADE,
        opp_player int references Players(id) ON DELETE CASCADE,
	result int
	CHECK (player <> opp_player)
  );

--Create wins view
  CREATE VIEW wins as 
	SELECT Players.id, COUNT(Matches.opp_player) AS n 
	FROM Players
	LEFT JOIN (SELECT * FROM Matches WHERE result>0) as Matches
	ON Players.id = Matches.player
	GROUP BY Players.id;

--Create total_matches view
  CREATE VIEW total_matches as
	SELECT Players.id, Count(Matches.opp_player) AS n 
	FROM Players
	LEFT JOIN Matches
	ON Players.id = Matches.player
	GROUP BY Players.id;
--Create player_standings view 
  CREATE VIEW player_standings as
	SELECT Players.id,Players.player_name,CAST (wins.n AS INTEGER) as wins,
        CAST(total_matches.n as INTEGER) as matches 
	FROM Players,total_matches,Wins
	WHERE Players.id = Wins.id and Wins.id = total_matches.id
	ORDER BY wins DESC;
