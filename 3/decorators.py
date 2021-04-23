#  simplest form of decorator
def null_decorator(func):
    return func

def greet():
    return 'Hello'

greet = null_decorator(greet)

# python @syntax for decorating function
@null_decorator
def greet():
    return 'Hello'

# decorators can modify behaviour
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

# applying multiple decorators
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello'

# decorators that accept arguments
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

# debuggable decorators
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'
    