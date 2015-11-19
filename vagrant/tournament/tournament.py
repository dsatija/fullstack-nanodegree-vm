#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import pdb


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection and
    cursor."""
    try:
        db = psycopg2.connect("dbname = {}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error in connecting with database")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = 'DELETE FROM Matches;'
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query = 'DELETE FROM Players'
    cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = 'SELECT COUNT(id) from Players'
    cursor.execute(query)
    rows = cursor.fetchone()
    db.close()
    return rows[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    query = "Insert into Players(player_name) values (%s);"
    parameter = (name, )
    cursor.execute(query, parameter)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = 'Select * from player_standings;'
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    query_1 = 'Insert into Matches(Player, opp_player, result) values (%s, %s, 1)'
    query_2 = 'Insert into Matches(Player, opp_player, result) values (%s, %s, 0)'
    params_1 = (winner, loser)
    params_2 = (loser, winner)
    cursor.execute(query_1, params_1)
    cursor.execute(query_2, params_2)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

i    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, cursor = connect()
    standings = playerStandings()
    db.close()
    i = 0
    pairings = []
    count = len(standings)
    """Checking if the no.of Players are even"""
    if(count % 2 == 0):
        while i < count:
            player_id1 = standings[i][0]
            player_name1 = standings[i][1]
            player_id2 = standings[i+1][0]
            player_name2 = standings[i+1][1]
            pairings.append((player_id1, player_name1,
                            player_id2, player_id1))
            i = i + 2
    return pairings
