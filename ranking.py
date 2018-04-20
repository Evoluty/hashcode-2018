from consts import *
from input import next_line, import_input
from collections import Counter


def rank(input_file, output_file):
    score = 0
    import_input(input_file)

    with open(output_file, 'r') as f:
        line = next_line(f)
        cnt_loop = 0
        while line:
            line = list(map(int, line))

            number_of_rides = line.pop(0)
            rides = line

            if number_of_rides != len(rides):
                raise Exception("Declared number of rides ({}) "
                                "doesn't match the number of ride "
                                "identifiers ({}) at line {}".format(number_of_rides, len(rides), cnt_loop))

            cnt = Counter(rides)
            for ride_id, times in cnt.items():
                if times > 1:
                    raise Exception('Error: Ride {} is assigned to a vehicle '
                                    'more than once at line {}'.format(ride_id, cnt_loop))

            current_car = V.cars[cnt_loop]
            for r in rides:
                # Save old values
                current_ride = V.rides[r]
                before_step, ride_length = current_car.current_step, current_ride.get_length()
                if current_car.current_intersection != current_ride.start:
                    before_step += Intersection.distance_between(current_car.current_intersection, current_ride.start)

                if current_car.add_ride(current_ride):
                    V.rides[r] = None
                    score += ride_length
                    if before_step == current_ride.earliest_start:
                        score += V.bonus
                else:
                    raise Exception('Error: Cannot add ride {} in line {}'.format(r, cnt_loop))

            line = next_line(f)
            cnt_loop += 1

    return score
