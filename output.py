from consts import *


# Export global variables into output file
def export_output(file_name):
    with open(file_name, 'w') as f:
        for car in V.cars:
            if len(car.rides) == 0:
                f.write("0\n")
            else:
                rides = " ".join(map(str, [r.id for r in car.rides]))
                f.write("{} {}\n".format(len(car.rides), rides))
