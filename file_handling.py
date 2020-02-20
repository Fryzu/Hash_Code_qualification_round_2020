from tqdm import tqdm


def read(file_name):

    with open('input/'+file_name, 'r') as f:
        total_num_books, num_libraries, num_days = (int(x) for x in f.readline().split())
        books_scores = {i: int(k) for i, k in enumerate(f.readline().split())}
        books_scores = {k: v for k, v in sorted(books_scores.items(), key=lambda item: item[1], reverse=True)}
        libraries = {k: dict.fromkeys(['num_books', 'signup_duration', 'scanning_speed', 'books',
                                       'score_per_day', 'books_score']) for k in range(num_libraries)}
        for i in range(num_libraries):
            libraries[i]['num_books'], libraries[i]['signup_duration'], libraries[i]['scanning_speed'] =\
                [int(x) for x in f.readline().split()]
            books = tuple([int(x) for x in f.readline().split()])
            libraries[i]['books'] = books
            books_score = sum([books_scores[book] for book in books])
            libraries[i]['books_score'] = books_score
            libraries[i]['score_per_day'] = books_score * libraries[i]['scanning_speed'] // libraries[i]['num_books']

    return total_num_books, num_libraries, num_days, books_scores, libraries


def write(file_name, data):
    num_libraries, libraries = data
    with open('output/'+file_name, 'w') as f:
        f.write(str(num_libraries) + '\n')
        for library_id, library in libraries.items():
            f.write(str(library_id) + ' ' + str(library['num_scanned_books']) + '\n')
            f.writelines([str(x) + ' ' for x in library['scanned_books']])
            f.write('\n')

