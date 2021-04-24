# simple example of list comprehension
squares = [x * x for x in range(10)]

# list comprehension with condition
even_squares = [x * x for x in range(10) if x % 2 == 0]

# set comprehension
sets = {x * x for x in range(-9, 10)}

# dict comprehension
dictionary = {x: x * x for x in range(5)}