# not a good way
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


# better way
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return "__repr__ for Car"

    def __str__(self):
        return "__str__ for Car"


# best way
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r}, {self.mileage!r})"

    def __str__(self):
        return f"a {self.color} car"
