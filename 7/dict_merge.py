xs = {"a": 1, "b": 2}
ys = {"b": 3, "c": 4}

# classical solution
zs = {}
zs.update(xs)
zs.update(ys)

# unpacking argument, most efficient
zs = {**xs, **ys}