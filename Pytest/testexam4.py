import pytest

class TestExam:

    def test_func1(self):

        x = 'python'

        assert 'y' in x

    def test_func2(self):

        x = 'python'
        assert hasattr(x, 'python')
