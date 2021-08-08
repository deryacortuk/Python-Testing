import pytest

@pytest.mark.parametrize("x,y,z",[(7,17,71),(3,4,7),(19,11,30)])
def test_func(x,y,z):
    assert x+y == z

@pytest.mark.parametrize("test,result", [("3*5", 15), ("2*4", 8), ("6+9", 42)])
def test_eval(test, result):
    assert eval(test) == result


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    assert x*y == 0 or 6

