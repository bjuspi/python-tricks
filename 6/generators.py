# infinite generator
def repeater(value):
    while True:
        yield value


# bounded generator
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
