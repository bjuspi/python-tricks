# built-in dictionaries
phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}

# ordered dict preserve the insertion order of keys
# must be imported from the collections module
import collections

d = collections.OrderedDict(one=1, two=2, three=3)

# default dict returns default callable
# when key is not found
dd = collections.defaultdict(list)
print(dd["sdfsd"])

# chain map groups multiple dictionaries
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = collections.ChainMap(dict1, dict2)

# mapping proxy type creates read-only dictionary
writable = {"one": 1, "two": 2}
read_only = collections.MappingProxyType(writable)