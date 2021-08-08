import pytest


def test_func():

    x = 17
    y = 17

    assert x == y

def test_func1():
    x = 12
    y = 10

    assert x**2 == y**3


# 'pytest -k test_func1  testexam2.py' 
# Name-based filtering:  You can do this with the -k parameter.