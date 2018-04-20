from input import import_input
from solution import solve
from output import export_output
from ranking import rank


def main():
    total = 0
    input_files = []
    # input_files.append("a_example.in")
    input_files.append("b_should_be_easy.in")
    # input_files.append("c_no_hurry.in")
    # input_files.append("d_metropolis.in")
    # input_files.append("e_high_bonus.in")

    for file in input_files:
        print("Working on: [{}]".format(file))

        print("- Importing...")
        # import_input("inputs/{}".format(file))

        print("- Solving...")
        # solve()

        print("- Exporting...")
        # export_output("outputs/{}".format(file.replace(".in", ".out")))

        print("- Ranking ...")
        score = rank("inputs/{}".format(file), "outputs/{}".format(file.replace(".in", ".out")))
        print("Score: {:,}\n".format(score).replace(',', ' '))
        total += score

    print("Your final score is: {:,}".format(total).replace(',', ' '))


if __name__ == '__main__':
    main()
