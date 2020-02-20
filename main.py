from file_handling import read, write
from solvers import simple


def main():
    input_files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']

    # Dynamic programming
    for input_file in input_files[:3]:
        input_data = read(input_file)
        solution = simple(input_data)
        write(input_file, solution)

    # Greedy algorithm
    for input_file in input_files[3:]:
        input_data = read(input_file)
        solution = simple(input_data)
        write(input_file, solution)


if __name__ == '__main__':
    main()
