class Library:
    def __init__(self, index, books, signup, scan_per_day):
        self.index = int(index)
        self.books = [int(x) for x in books]
        self.signup = int(signup)
        self.scan_per_day = int(scan_per_day)
