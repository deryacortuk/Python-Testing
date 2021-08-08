import pytest

#pytest.mark.NAME  --->  Simple MarkDecorator


@pytest.mark.seven
def test_func():

    x = 3
    y = 7

    assert x*y == y**2

@pytest.mark.sieben
def test_test1():

    x = 2
    y = 7

    assert x*y == y*x