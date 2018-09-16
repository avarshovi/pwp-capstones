# Capstone project for Codeacademy Programming with Python (Intensive)
# Ali Varshovi (avarshovi)


import re


class User(object):

    def __init__(self, name, email):
        if self._is_valid_email(email):
            self.email = email.lower()  # Store email as all lower case
        else:
            return
        self.name = name.title()  # Name is string. Store in title case.
        self.books = {}  # Dict with Book objects as keys and current user ratings as values

    # Checks for the validity of an email address using regex
    def _is_valid_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address")
            return False
        return True

    def get_email(self):
        return self.email

    def change_email(self, address):
        if self._is_valid_email(address):
            self.email = address
        return

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for rating in self.books.values():
            if rating is not None:
                total += rating
        return total / len(self.books)

    def get_number_of_books_read(self):
        return len(self.books)

    def get_worth(self):
        worth = 0
        for book in self.books.keys():
            worth += book.price
        return worth

    def __repr__(self):
        return "User {name}, email: {email} with {reviews} book reviews".format(
            name = self.name, email = self.email, reviews = len(self.books)
        )

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email


class Book(object):
    def __init__(self, title, isbn, price = 0):
        self.title = title.title()  # Title is a string in Title case
        self.isbn = isbn  # ISBN is a string
        self.ratings = []  # Ratings is a list of all the ratings given to a Book object by the Users
        self.price = price  # Price is an Integer

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn

        '''
        Used a regular expression to check for the validity of the ISBN.
        Commented out as it doesn't work with the sample data given.
        This would work with standard ISBN format.
        
         if not re.match(r"978(?:-?\d){10}", new_isbn):
            return 0
         else:
            self.isbn = new_isbn
            return 1
        '''

    def set_price(self, new_price):
        self.price = new_price

    def add_rating(self, rating):
        if rating in range(0, 5) or rating is None:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            if rating is not None:
                total += rating
        return total / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __repr__(self):
        return "{title}, ISBN: {isbn}, Price: ${price}".format(title = self.title,
                                                               isbn = self.isbn, price = self.price)


class Fiction(Book):
    def __init__(self, title, author, isbn, price = 0):
        super().__init__(title, isbn, price)
        self.author = author.title()  # Author is a string in Title case

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}, Price: ${price}".format(title = self.title,
                                                             author = self.author, price = self.price)


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn, price = 0):
        super().__init__(title, isbn, price)
        self.subject = subject  # Subject is a String
        self.level = level  # Level is a string

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}, Price: ${price}".format(
            title = self.title, level = self.level, subject = self.subject, price = self.price
        )


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    # Printing a TomeRater object. This will print the TomeRater Catalog and Users.
    def __repr__(self):
        print("\nTome Rater")
        print("\nCatalog:")
        self.print_catalog()
        print("\nUsers:")
        self.print_users()
        return ""

    # Checking if two TomeRaters are equal by comparing users and books dictionaries.
    def __eq__(self, other_tr):
        return self.users == other_tr.users \
               and self.books == other_tr.books

    # Method to check if a given ISBN is unique in the TomeRater.
    def _is_unique_isbn(self, isbn):
        for book in self.books.keys():
            if isbn == book.isbn:
                print("Provided ISBN is not unique.")
                return False
        return True

    def create_book(self, title, isbn, price = 0):
        if self._is_unique_isbn(isbn):
            return Book(title, isbn, price)
        return 0

    def create_novel(self, title, author, isbn, price = 0):
        if self._is_unique_isbn(isbn):
            return Fiction(title, author, isbn, price)
        return 0

    def create_non_fiction(self, title, subject, level, isbn, price = 0):
        if self._is_unique_isbn(isbn):
            return NonFiction(title, subject, level, isbn, price)
        return 0

    def add_book_to_user(self, book, email, rating = None):
        try:
            user = self.users[email.lower()]
        except KeyError:
            print("No user with email {email}".format(email = email))
            return 0

        user.read_book(book, rating)
        book.add_rating(rating)
        if book in self.books.keys():
            self.books[book] += 1
        else:
            self.books.update({book: 1})

    def add_user(self, name, email, user_books = None):
        if email in self.users.keys():
            print("User already exists.")
            return
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    # Internal method to aid both get_most_read_book and get_n_most_read_books
    def _most_read_book(self, books):
        max_read = 0
        book = None
        for item in books.keys():
            if books[item] > max_read:
                max_read = books[item]
                book = item
        return book

    def _most_expensive_book(self, books):
        max_price = 0
        book = None
        for item in books.keys():
            current_price = item.get_price()
            if current_price > max_price:
                max_price = current_price
                book = item
        return book

    def get_most_read_book(self):
        return self._most_read_book(self.books)

    def get_n_most_read_books(self, n):
        books = self.books.copy()
        n_books = []
        i = 0
        while i <= n-1 and len(books) > 0:
            current_most_read = self._most_read_book(books)
            n_books.append(current_most_read)
            books.pop(current_most_read)
            i += 1
        return n_books

    def get_highest_rated_book(self):
        book = None
        highest = 0
        for item in self.books.keys():
            current_avg = item.get_average_rating()
            if current_avg > highest:
                highest = current_avg
                book = item
        return book

    def get_n_most_expensive_books(self, n):
        books = self.books.copy()
        n_books = []
        i = 0
        while i <= n-1 and len(books) > 0:
            current_most_expensive = self._most_expensive_book(books)
            n_books.append(current_most_expensive)
            books.pop(current_most_expensive)
            i += 1
        return n_books

    def _most_prolific_reader(self, users):
        max_number = 0
        user = None
        for item in users.values():
            books_read = item.get_number_of_books_read()
            if books_read > max_number:
                max_number = books_read
                user = item
        return user

    def get_most_positive_user(self):
        user = None
        highest = 0
        for item in self.users.values():
            current_avg = item.get_average_rating()
            if current_avg > highest:
                highest = current_avg
                user = item
        return user

    def get_n_most_prolific_readers(self, n):
        users = self.users.copy()
        n_users = []
        i = 0
        while i <= n-1 and len(users) > 0:
            current_prolific = self._most_prolific_reader(users)
            n_users.append(current_prolific)
            users.pop(current_prolific.get_email())
            i += 1
        return n_users

    def get_worth_of_user(self, user_email):
        return self.users[user_email].get_worth()



