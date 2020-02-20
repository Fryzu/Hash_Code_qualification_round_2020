from tqdm import tqdm


def solve_greedy(num_days, books_scores, libraries):
    scanned_libraries = dict()
    scanned_books_general = set()
    day = 0
    for k, v in tqdm(libraries.items()):
        day += v['signup_duration']
        num_days_scanning = max(num_days - day, 0)
        if num_days_scanning != 0:
            max_scanned_books = num_days_scanning * v['scanning_speed']
            num_scanned_books = min(max_scanned_books, len(v['books']))
            scanned_books = []
            cnt = 0
            set_books = set(v['books'])
            for book_id, book_score in books_scores.items():
                if cnt >= num_scanned_books:
                    break
                if book_id in set_books and book_id not in scanned_books_general:
                    scanned_books.append(book_id)
                    scanned_books_general.add(book_id)
                    cnt += 1
            if len(scanned_books) != 0:
                scanned_libraries[k] = {'num_scanned_books': cnt,
                                        'scanned_books': scanned_books}
    return scanned_libraries
