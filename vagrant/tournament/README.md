Udacity Full Stack Web Developer Nanodegree Project 2
 
Swiss Tournament Results

Files

tournament.py -- implementation of a Swiss-system tournament
tournament.sql -- tables and views definitions for the tournament project.
tournament_test.py -- Test cases for tournament.py

Usage

Make sure database "tournament" exists

Command to run the program:

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ 
python tournament_test.py

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
