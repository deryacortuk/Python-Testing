import pytest

def func(*args):
    return args

def test_func():
    assert func(2,3,4,5,6)== (2,3,4,5,6)
