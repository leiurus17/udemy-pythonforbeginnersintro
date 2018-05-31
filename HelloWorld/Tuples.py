# Tuples are immutable

tup1 = ("Oranges", "Apples", "Bananas")

print(tup1)

# but you can concatenate tuples
# You can delete tuples but you cannot modify
# The contents of tuples

tup2 = ("Melons", "Watermelons")
tup3 = ("Lemons", "Mangoes")

# Apparently, you can't concat a single-containing tuple
# Because it is considered only as a string

tup5 = ("Forbidden Fruit")

print(tup5)

tup4 = tup1 + tup2 + tup3

print(tup4)