import pytest

@pytest.fixture           #Decorator to mark a fixture factory function.This decorator can be used, with or without parameters, to define a fixture function.
def func():
    nlist = [2,3,5,7]
    return nlist

@pytest.mark.skip
def test_func(func):

    x = 7

    assert func[1] == x


def test_func1(func):
    x = 7

    assert func[3] == x

def test_func3(func):
    x =3
    assert func[1] == x

def test_func4(func):
    x =3
    assert func[0] == x

@pytest.mark.xfail
def test_func5(func):
    x =3
    assert func[2] == x








    
