# Single leading underscore _var
# single leading underscore is meant for internal user, it is generally not enforced 
# by the Python interpreter and is only meant as a hint to the programmer.
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


# Single trailing underscore var_
# single trailing underscore is used by convention to avoid naming conflicts
# with Python keywords.
def make_object(name, class_):
    pass


# Double leading underscore __var
# double leading underscore causese the Python interpreter to rewrite the
# attribute name of the variable, or 'name mangling'
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42

t = Test()
print(dir(t))


# Double leading and trailing underscore __var__
# reserved for python magic methods, like __init__
class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42


# Single underscore _
# temporary variable
for _ in range(32):
    print('Hello, World.')
