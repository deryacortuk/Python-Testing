import unittest
from .data_class import func


class TestMock(unittest.TestCase):
    
   
    def test_func(self):
        result = func()

        self.assertEqual(result,(1, "It is test1"))

if __name__ == '__main__':
    unittest.main()