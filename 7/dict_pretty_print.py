mapping = {"a": 23, "b": 42, "c": 0xC0FFEE}

# traditional way
print(str(mapping))

# slightly better way
import json

json.dumps(mapping, indent=4, sort_keys=True)

# classical solution
import pprint

pprint.pprint(mapping)