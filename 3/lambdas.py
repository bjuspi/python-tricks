# example of lambda function
def add(x, y):
    return x + y

add = lambda x, y: x + y

# the advantage of lambda expression is not assigning function name
add(5, 3)
(lambda x,y: x + y)(5,3)

# example of using lambda expression
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))

# lamdas also capture local state, lexical closures
def make_adder(n):
    return lambda x: x + n