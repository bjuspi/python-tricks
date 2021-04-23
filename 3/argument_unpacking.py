def print_vector(x, y, z):
    print("<%s, %s, %s>" % (x, y, z))


tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
dict_vec = {"y": 0, "z": 1, "x": 1}

# unefficient
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
print_vector(dict_vec["x"], dict_vec["y"], dict_vec["z"])

# better
print_vector(*tuple_vec)
print_vector(*list_vec)
print_vector(**dict_vec)
