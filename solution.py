from consts import *


# Resolve the problem and put correct global variables
def solve():
    for ride in V.rides:
        for car in V.cars:
            if car.add_ride(ride):
                break
