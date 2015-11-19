Udacity Full Stack Web Developer Nanodegree Project 2
 
This project serves the purpose of ranking the swiss tournament players and provide results.

Files-

tournament.py -- implementation of a Swiss-system tournament
tournament.sql -- tables and views definitions for the tournament project.
tournament_test.py -- Test cases for tournament.py

Usage

Below are the requirements for running this project:
1)Postgresql
2)Python(2.7 or 3.0) installation
3)Setup using vagrant and virtual box can be done.

Command to run the program:
1)copy the contents of this repository to virtual machine forder /vagrant/tournment/
2) create the database ,tables and views used in this project by running--
psql -f tournament.sql
3)run the application using below command:
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ 
python tournament_test.py

RESULTS:

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
