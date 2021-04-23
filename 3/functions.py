# functions are objects
# function object referenced by yell
def yell(text):
    return text.upper() + '!'

# bark referenced to yell
bark = yell

# functions stored in data structured
funcs = [bark, str.lower, str.capitalize]

# functions passed to other functions
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

# functions nested in other functions
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

# functions returning nested functions
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

# functions capturing local state
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

# callable object
class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4)) # execute __call__ method
print(callable(plus_3))
