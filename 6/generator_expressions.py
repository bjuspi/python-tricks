# simple generator expressions
iterator = ("Hello" for i in range(3))

# filtering values for simple generator expressions
even_squares = (x * x for x in range(10) if x % 2 == 0)

# in-line expressions
for x in ("hello" for i in range(3)):
    print(x)

# parantheses can be dropped in a single argument function
sum((x * 2 for x in range(10)))
sum(x * 2 for x in range(10))