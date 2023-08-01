import pytest 
from pythonic import *

def test_collection():
    collection = Collection()
    collection.add_item(1)
    collection.add_item(2)
    collection.add_item(3)

    assert list(collection) == [1, 2, 3]
    assert [item ** 2 for item in collection] == [1, 4, 9]
    assert list(collection) == [1, 2, 3]

def test_point():
    point1 = Point(1, 2)
    point2 = Point(1, 2)
    assert point1 == point2
    assert bool(point1) == True

def test_math():
    math = Math()
    math.adder(5)
    math.multiplier(3)
    math.squared(2)

    assert math.sum == 5
    assert math.product == 15
    assert math.squares == [4]

def test_say():
    assert say("great") == 'That is, "great"'
