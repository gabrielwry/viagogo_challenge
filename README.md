**Viagogo Developer Chllenge:**
9/27/2017

This program randomly generated a world of size 20*20 (x in range[-10,10] and y in rnage[-10,10], allowing 1 float point);<br  />
The default capacity of event at each location is set to 1;<br  />
Event size is an arbitray choice smaller than the world's capacity;<br  />
Each event has 100 tickets;<br  />
Each ticket has a price ranging (0,500];<br  />

The solve method asks user for x and y coordinates input and print out the 5 closest events with cheapest ticket and distance from user;<br  />
Distances are calculated as Manhattan Distance;<br  />

To optimize, the cheapest ticket is stored each time a ticket is added to the event.<br  />

Python 3 Command Line Usage:
```
python solution.py
```
Sample Command Line Running on windows terminal:
```
.\viagogo_challenge>python solution.py
The world is built.
Please enter your x coordinate,ranging from -10.0 to 10.0 and y coordinate ranging from -10.0 to 10.0 (format:x,y):1,2
User location is (1.0,2.0)
Event id: 120- $4.34, Distance 1.1
Event id: 157- $9.73, Distance 1.7
Event id: 203- $5.11, Distance 0.6
Event id: 289- $5.92, Distance 1.3
Event id: 483- $1.56, Distance 1.5
```
