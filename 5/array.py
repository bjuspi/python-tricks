# built-in dynamic array/list,  mutable
arr = ["one", "two", "three"]

# built-in tuples, immutable
arr = ("one", "two", "three")

# mutable typed array
import array

arr = array.array("f", (1.0, 1.5, 2.0, 2.5))

# immutable array of unicode characters
arr = "abcd"

# immutable array of single bytes
arr = bytes((0, 1, 2, 3))

# mutable array of single bytes
arr = bytearray((0, 1, 2, 3))