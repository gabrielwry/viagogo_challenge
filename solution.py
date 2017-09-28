"""
Viagogo Developer Chllenge:
9/27/2017
Generating Random Seed Data method: generateData()

Initiating World: initate(north,south,east,west)
Location Objects: class Location
Event Objects: class Event
Ticket Objects: class Ticke

Solution method: findClosestEvents(x,y)

Command Line usage: python solution.py x_coordinate,y_coordinate
"""
import sys
import math
import random

# Define global variables, default world size, helper functions
DEFAULT_HEIGHT = 10.0
DEFAULT_WIDTH = 10.0
FLOAT_POINT = 1 # allowing one float point percision
CAPACITY = 1  # allowing one event at each location
EVENT_SIZE = 1000000  # allowing 500 events by default
TICKET_SIZE = 100  # allowing 100 tickets per event by default
TICKET_PRICE_RANGE = 500.0  # default price range 0~500


def manhattan_distance(location_1, location_2):
    """
    :param location_1: Location object
    :param location_2: Location object
    :return: manhattan distance between two locations
    :rtype float
    """
    return abs(location_1.x - location_2.x) + abs(location_1.y - location_2.y)

# define objects


class Location:
    def __init__(self,x,y):
        """
        :param x: float
        :param y: float
        """
        self.x = x
        self.y = y
        self.events = []

    def able_to_add_event(self):
        """
        :return: boolean
        """
        return len(self.events) < CAPACITY

    def add_event(self,event):
        """
        :param event: Event object
        """
        self.events.append(event)

    def __str__(self):
        return str(self.x)+','+str(self.y)


class Event:
    def __init__(self,id_,location,tickets=[]):
        """
        :param id_:integer
        :param location: Location object
        :param tickets: list of tickets objects
        """
        self.id = id_
        self.tickets = tickets
        self.cheapest_ticket = None


    def set_cheapest(self,ticket):
        """
        :param ticket: Ticket object
        """
        self.cheapest_ticket = ticket


    def get_cheapest(self):
        """
        :return: cheapest ticket
        """
        return self.cheapest_ticket


    def __str__(self):
        str_ = 'Event id: '+str(self.id).zfill(3)+'- '+str(self.cheapest_ticket)
        return str_


class Ticket:
    def __init__(self,id_,price):
        """
        :param price:float
        """
        self.id_ = id_
        self.price = price

    def __str__(self):
        return '${:,.2f}'.format(self.price)


class World:
    def __init__(self):
        self.locations_with_events=[]
        for i in range(1,EVENT_SIZE+1):
            while True:
                x = float('{:,.1f}'.format(random.uniform(-10.0,10.0)))
                y = float('{:,.1f}'.format(random.uniform(-10.0, 10.0)))
                location = Location(x,y)
                if location.able_to_add_event():
                    tickets = []
                    cheapest = float('inf')
                    cheapest_ticket = None
                    for j in range(0, TICKET_SIZE + 1):
                        price = TICKET_PRICE_RANGE * random.random()
                        ticket = Ticket(j,price)
                        if price <= cheapest:
                            cheapest = price
                            cheapest_ticket = ticket
                        tickets.append(ticket)
                    event = Event(i, location, tickets)
                    event.set_cheapest(cheapest_ticket)
                    location.add_event(event)
                    self.locations_with_events.append(location)
                    break
        print ('The world is built.')


def solve(world):
    """
    :param world: World object
    :return: list of 5 closet events with cheapest ticket price of each event
    """
    # Read in user input
    x_coordinate = 0.0
    y_coordinate = 0.0
    try:
        coordinates = raw_input('Please enter your x coordinate,ranging from {:,.1f} to {:,.1f} '
                                'and y coordinate ranging from {:,.1f} to {:,.1f} (format:x,y):'
                                .format(-DEFAULT_WIDTH,DEFAULT_WIDTH,-DEFAULT_HEIGHT,DEFAULT_HEIGHT)).split(',')
        x_coordinate = float(coordinates[0])
        y_coordinate = float(coordinates[1])
        if not -10.0 <= x_coordinate <= 10.0 or not -10.0 <= y_coordinate <= 10.0:
            print ('One of your coordinates is out of range, '
                   'please only enter coordinates that ranges from -10.0 to 10.0 both x and y.')
    except IndexError:
        print('Input not valid, please make sure you type in TWO coordinates separated by a COMMA.')
    user_location = Location(x_coordinate,y_coordinate)
    closest = [(None,float('inf'))]*5
    for each in world.locations_with_events:
        distance = manhattan_distance(each,user_location)
        max_ = max(closest,key = lambda x: x[1])
        if distance <= max_[1]:
            closest.remove(max_)
            closest.append((each,distance))
    return closest


def main():
    try:
        assert EVENT_SIZE <= CAPACITY * (2 * DEFAULT_HEIGHT) * (2 * DEFAULT_WIDTH) * ((10 ** FLOAT_POINT) ** 2)
    except AssertionError:
        print('Event size larger than world capacity.')
        sys.exit(0)
    world = World()
    closest_five_events = solve(world)
    for (location,distance) in closest_five_events  :
        for event in location.events:
            print str(event)+', Distance {:,.1f}'.format(distance)


if __name__ == "__main__": main()
