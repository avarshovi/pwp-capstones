from TomeRater import *

Tome_Rater1 = TomeRater()

#Create some books:
book1 = Tome_Rater1.create_book("Society of Mind", 12345678, 10)
novel1 = Tome_Rater1.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 20)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater1.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 50)
nonfiction2 = Tome_Rater1.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 20)
novel2 = Tome_Rater1.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater1.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater1.add_user("Alan Turing", "alan@turing.com")
Tome_Rater1.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater1.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater1.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater1.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater1.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater1.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater1.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater1.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater1.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater1.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
# Tome_Rater1.print_catalog()
# Tome_Rater1.print_users()

# print("Most positive user:")
# print(Tome_Rater1.most_positive_user())
# print("Highest rated book:")
# print(Tome_Rater1.highest_rated_book())
# print("Most read book:")
# print(Tome_Rater1.get_most_read_book())



Tome_Rater2 = TomeRater()

#Create some books:
book1 = Tome_Rater2.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater2.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater2.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater2.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater2.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater2.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater2.add_user("Alan Turing", "alan@turing.com")
Tome_Rater2.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater2.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater2.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater2.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater2.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater2.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
# Tome_Rater2.print_catalog()
# Tome_Rater2.print_users()

# print("Most positive user:")
# print(Tome_Rater2.most_positive_user())
# print("Highest rated book:")
# print(Tome_Rater2.highest_rated_book())
# print("Most read book:")
# print(Tome_Rater2.get_most_read_book())
