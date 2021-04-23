# shallow copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
# ys = copy.copy(xs)

# deep copy
import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
