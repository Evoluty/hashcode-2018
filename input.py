from consts import *


# Reads next line of a given file and returns an array of words
def next_line(file):
    res = file.readline()
    if res:
        res = res.replace('\n', "").split(" ")
    return [elem for elem in res if elem]


# Import data from input files into global variables
def import_input(file_name):
    with open(file_name, 'r') as f:
        # Read first line
        first_line = next_line(f)
        V.number_rows, V.number_columns, V.number_vehicles, V.number_rides, V.bonus, V.number_steps = map(int, first_line)
        V.cars = [Car() for _ in range(V.number_vehicles)]

        # Read rides
        V.rides = []
        for i in range(V.number_rides):
            line = next_line(f)
            start_r, start_c, end_r, end_c, earliest, latest = map(int, line)
            ride = Ride(i, start_r, start_c, end_r, end_c, earliest, latest)

            V.rides.append(ride)
