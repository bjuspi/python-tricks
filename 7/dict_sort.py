xs = {"a": 4, "c": 2, "b": 4, "d": 1}

# sorting by key
sorted(xs.items())

# sorting by value
sorted(xs.items(), key=lambda x: x[1])

# sorting by value, larger values go first
sorted(xs.items(), key=lambda x: x[1], reverse=True)