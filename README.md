**Viagogo Developer Chllenge:**
9/27/2017

This program randomly generated a world of size 20*20 (x in range[-10,10] and y in range[-10,10], allowing 1 float point);<br  />
The default capacity of events at each location is set to 1;<br  />
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
Please enter your x coordinate,ranging from -10.0 to 10.0 and y coordinate ranging from -10.0 to 10.0 (format:x,y):3,4
User location is (3.0,4.0)
Event id: 051- $1.10, Distance 0.6
Event id: 078- $4.43, Distance 1.2
Event id: 141- $11.37, Distance 0.7
Event id: 230- $9.47, Distance 1.1
Event id: 476- $9.56, Distance 0.7
Do you want to query another location? (N/Y)   Y
Please enter your x coordinate,ranging from -10.0 to 10.0 and y coordinate ranging from -10.0 to 10.0 (format:x,y):2,3
User location is (2.0,3.0)
Event id: 038- $45.72, Distance 0.7
Event id: 051- $1.10, Distance 1.6
Event id: 078- $4.43, Distance 0.8
Event id: 229- $0.03, Distance 0.7
Event id: 467- $5.31, Distance 0.6
Do you want to query another location? (N/Y)   N
Thanks for using.
```
-The world only supports one event at each location for now. <br   />
The default setting of event capacity of each location is declared in the program. The program keeps a list of events at each location and already support multiple events.<br     />

-The world size right now is relatively small.<br   />
If the world size gets larger, one way to optimize the calculation speed is to exapnding the radius recursively at the user location instead of searching the whole world.<br   />
For example, the user location is (0.0,0.0), we first did a search at radius 1 and see if there are 5 matching events and grows the radius to 2 if there is not. This method may work well given the density of the events is large.
