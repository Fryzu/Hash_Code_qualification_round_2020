from file_handling import read, write
from solvers import solve_greedy


def main():
    input_files = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt',
                   'f_libraries_of_the_world.txt']

    for input_file in input_files[:3]+input_files[4:5]:
        total_num_books, num_libraries, num_days, books_scores, libraries = read(input_file)
        libraries = {k: v for k, v in sorted(libraries.items(),
                                             key=lambda item: item[1]['signup_duration'], reverse=False)}
        solution = solve_greedy(num_days, books_scores, libraries)
        write(input_file, (len(solution.keys()), solution))

    for input_file in input_files[3:4]+input_files[-1:]:
        total_num_books, num_libraries, num_days, books_scores, libraries = read(input_file)
        libraries = {k: v for k, v in sorted(libraries.items(),
                                             key=lambda item: item[1]['books_score'] - item[1]['signup_duration']
                                                              * item[1]['score_per_day'], reverse=True)}
        solution = solve_greedy(num_days, books_scores, libraries)
        write(input_file, (len(solution.keys()), solution))


if __name__ == '__main__':
    main()
