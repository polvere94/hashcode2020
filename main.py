from Library import Library


class Result:
    def __init__(self, library_num, books):
        self.library_num = library_num
        self.books = books

    def __str__(self):
        return f'{self.library_num} - {self.books}'



def main():
    filename='d_tough_choices.txt'
    output_filename = 'out_d.txt'

    f = open(filename, "r")
    NoBooks, lib, scanDays = f.readline().split()
    values = f.readline().split()
    book_values = {i: int(y) for i, y in enumerate(values)}


    libraries = []
    for i in range(int(lib)):
        lib_Books, sign_Days, ship_Quant = f.readline().split()
        books = f.readline().split()
        libraries.append(Library(i, books, sign_Days, ship_Quant))


    deadline = int(scanDays)
    # libraries = [
    #     Library(0, [0, 1, 2, 3, 4], 2, 2),
    #     Library(1, [3, 2, 5, 0], 3, 1),
    # ]
    # book_values = {0: 1,
    #                1: 2,
    #                2: 3,
    #                3: 6,
    #                4: 5,
    #                5: 4}

    out = []

    while deadline > 0 and len(libraries) > 0:
        best_library = None
        choosed_books = []
        best_value = 0
        best_score = 0

        for library in libraries:
            if best_library is None:
                best_library = library
                choosed_books, best_value, best_score = library_value(library, book_values, deadline)
                continue
            tries_book, sum_, score = library_value(library, book_values, deadline)
            if score > best_score:
                best_library = library
                choosed_books = tries_book
                best_score = score

        # togliere i libri dalle altre librerie
        for book in choosed_books:
            book_values[book] = 0

        deadline = deadline - best_library.signup
        out.append(Result(best_library.index, choosed_books))
        libraries.remove(best_library)

    print([str(x) for x in out])

    out_file = open(output_filename, "w")
    out_file.write(str(len(out)))
    out_file.write('\n')
    for res in out:
        out_file.write(str(res.library_num) + ' ' + str(len(res.books)) + '\n')
        for book in res.books:
            out_file.write(str(book) + ' ')
        out_file.write('\n')


def library_value(library: Library, book_values: dict, deadline):
    days = deadline - library.signup
    score = 1-(library.signup/deadline)
    books = sorted(library.books, key=lambda x: book_values[x], reverse=True)
    nr = days * library.scan_per_day
    books = books[0:min(nr, len(books))]
    sum_ = sum([book_values[x] for x in books])
    return books, sum_ , score*sum_


if __name__ == '__main__':
    main()
