Viagogo Developer Chllenge:
9/27/2017

This program randomly generated a world of size 20*20 (x in range[-10,10] and y in rnage[-10,10], allowing 1 float point);
The default capacity of event at each location is set to 1;
Event size is an arbitray choice smaller than the world's capacity;
Each event has 100 tickets;
Each ticket has a price ranging (0,500];

The solve method asks user for x and y coordinates input and print out the 5 closest events with cheapest ticket and distance from user;
Distances are calculated as Manhattan Distance;

To optimize, the cheapest ticket is stored each time a ticket is added to the event.

Python 3 Command Line Usage: python solution.py
