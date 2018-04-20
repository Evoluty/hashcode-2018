# Global variables of the program
from pprint import pprint

class V:
    number_rows = 0
    number_columns = 0
    number_vehicles = 0
    number_rides = 0
    bonus = 0
    number_steps = 0

    cars = []
    rides = []


# Classes
class Intersection:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @staticmethod
    def distance_between(start, end):
        return abs(start.row - end.row) + abs(start.column - end.column)

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __repr__(self):
        return 'row: {}, col: {}'.format(self.row, self.column)


class Ride:
    def __init__(self, num, row_start, col_start, row_end, col_end, earliest_start, latest_end):
        self.id = num
        self.start = Intersection(row_start, col_start)
        self.end = Intersection(row_end, col_end)
        self.earliest_start = earliest_start
        self.latest_end = latest_end

    def get_length(self):
        return Intersection.distance_between(self.start, self.end)

    def __repr__(self):
        return 'id: {}\nstart: [{}]\nend: [{}]\nearliest_start: {}\nlastest_end: {}'.format(self.id, self.start, self.end, self.earliest_start, self.latest_end)


class Car:
    def __init__(self):
        self.rides = []
        self.current_step = 0
        self.current_intersection = Intersection(0, 0)

    def __repr__(self):
        return 'rides: [{}]\ncurrent_step:{}\ncurrent_intersection:{}'.format(self.rides, self.current_step, self.current_intersection)

    def step_when_added(self, ride):
        return self.current_step + ride.get_length() + \
            Intersection.distance_between(self.current_intersection, ride.start)

    def can_add_ride(self, ride):
        return self.step_when_added(ride) < ride.latest_end < V.number_steps

    def add_ride(self, ride):
        if self.can_add_ride(ride):
            self.rides.append(ride)
            self.current_step = self.step_when_added(ride)
            self.current_intersection = Intersection(ride.end.row, ride.end.column)
            return True
        return False

    def count_rides(self):
        return len(self.rides)
