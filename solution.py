import sys
import math
import random

# Define global variables, default world size, helper functions
DEFAULT_HEIGHT = 10.0
DEFAULT_WIDTH = 10.0
FLOAT_POINT = 1 # allowing one float point percision
CAPACITY = 1  # allowing one event at each location
EVENT_SIZE = 500  # allowing 500 events by default
TICKET_SIZE = 100  # allowing 100 tickets per event by default
TICKET_PRICE_RANGE = 500.0  # default price range 0~500
QUERY_NUMBER = 5 # default 5 closest events


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
        self.events = [] # Initiate a location with a blank list of events

    def able_to_add_event(self):
        """
        :rtype: boolean
        """
        return len(self.events) < CAPACITY # check number of events at a location

    def add_event(self,event):
        """
        :param event: Event object
        """
        self.events.append(event)

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


class Event:
    def __init__(self,id_,location,tickets=[]):
        """
        :param id_:integer
        :param location: Location object
        :param tickets: list of tickets objects
        """
        self.id = id_
        self.tickets = tickets
        self.cheapest_ticket = None # keep track of the cheapest ticket of this event

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

    def add_ticket(self, ticket):
        """
        :param tickets: Ticket object
        """
        self.tickets.append(ticket)
        if self.get_cheapest() is None or ticket.price <= self.cheapest_ticket.price:
            self.set_cheapest(ticket) # update the cheapest ticket when adding a ticket

    def __str__(self):
        str_ = 'Event id: '+str(self.id).zfill(3)+'- '+str(self.cheapest_ticket)
        return str_


class Ticket:
    def __init__(self, id_, price):
        """
        :param price:float
        """
        self.id_ = id_
        self.price = price

    def __str__(self):
        return '${:,.2f}'.format(self.price) # format ticket string


class World:
    def __init__(self):
        self.locations_with_events=[]
        for i in range(1,EVENT_SIZE+1):
            while True:
                x = float('{:,.1f}'.format(random.uniform(-10.0,10.0)))
                y = float('{:,.1f}'.format(random.uniform(-10.0, 10.0))) # initiate world with default setting
                location = Location(x,y)

                if location.able_to_add_event():
                    tickets = []
                    event = Event(i, location, tickets)

                    for j in range(0, TICKET_SIZE + 1):
                        price = TICKET_PRICE_RANGE * random.random()
                        ticket = Ticket(j,price)
                        event.add_ticket(ticket)

                    location.add_event(event)
                    self.locations_with_events.append(location)
                    break # keep adding events to a location until capacity
        print ('The world is built.') # notify user the world is built


def solve(world):
    """
    :param world: World object
    :return: list of 5 closet events with cheapest ticket price of each event
    """
    # Read in user input
    try:
        coordinates = raw_input('Please enter your x coordinate,ranging from {:,.1f} to {:,.1f} '
                                'and y coordinate ranging from {:,.1f} to {:,.1f} (format:x,y):'
                                .format(-DEFAULT_WIDTH,DEFAULT_WIDTH,-DEFAULT_HEIGHT,DEFAULT_HEIGHT)).split(',')

        x_coordinate = float(coordinates[0])
        y_coordinate = float(coordinates[1])

        if not -DEFAULT_WIDTH <= x_coordinate <= DEFAULT_WIDTH or not -DEFAULT_HEIGHT <= y_coordinate <= DEFAULT_HEIGHT:
            print ('One of your coordinates is out of range, '
                   'please only enter coordinates that range from -{:,.1f} to {:,.1f} for x '
                   'and -{:,.1f} to {:,.1f} for y.').format(DEFAULT_WIDTH,DEFAULT_WIDTH,DEFAULT_HEIGHT,DEFAULT_HEIGHT)
            sys.exit(0) # out of range error

    except (ValueError,IndexError):
        print('Input not valid, please make sure you type in TWO coordinates separated by a COMMA.')
        sys.exit(0) # invalid input number error

    user_location = Location(x_coordinate,y_coordinate)
    print 'User location is '+str(user_location)

    closest = [(None,float('inf'))]*QUERY_NUMBER # initiate with default
    for each in world.locations_with_events:
        distance = manhattan_distance(each,user_location)
        max_ = max(closest,key = lambda x: x[1]) # sort by distance and get the furthest event
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

    for (location,distance) in closest_five_events:
        for event in location.events:
            print str(event)+', Distance {:,.1f}'.format(distance)


if __name__ == "__main__": main()
