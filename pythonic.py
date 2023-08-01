from functools import wraps
import time
from time import sleep


# collection class using generators
class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        for item in self.items:
            yield item

# Decorator function to calculate time spent in a function
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

# Custom data structure with dunder methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __bool__(self):
        return self.x != 0 or self.y != 0

# Math class with adder, multiplier, and squared methods
class Math:
    def __init__(self):
        self.sum = 0
        self.product = 1
        self.squares = []

    def adder(self, value):
        self.sum += value

    def multiplier(self, value):
        self.product *= value

    def squared(self, value):
        self.squares.append(value**2)

# Procrastinate decorator
def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)
    return wrapper

# Sarcastic decorator
def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        return f'That is, "{output}"'
    return wrapper

@procrastinate
@sarcastic_decorator
def say(text):
    return text



if __name__ == "__main__":
    collection = Collection()
    collection.add_item(1)
    collection.add_item(2)
    collection.add_item(3)

    for item in collection:
        print(item)

    squared_items = [item ** 2 for item in collection]
    print(squared_items)

    list_collection = list(collection)
    print(list_collection)

    point1 = Point(1, 2)
    point2 = Point(1, 2)
    print(point1 == point2) 
    print(bool(point1)) 

    print("Running...")
    print(say("awesome."))
