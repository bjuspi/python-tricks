a = [1, 2, 3]
b = a
c = list(a)

a == b  # True
a is b  # True

a == c  # True
a is c  # False

# Just remember twin cats
