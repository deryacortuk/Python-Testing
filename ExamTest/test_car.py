import unittest

from .car import Car


class TestCar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        
    def setUp(self):
        self.car1 = Car('Ferrari',2022,'Black')
        self.car2 = Car('Bentley',2022,'Black')

    def tearDown(self):
        print('tearDown\n')

    def test_car(self):        

        self.assertEqual(self.car1.name,'Ferrari')
        self.assertEqual(self.car2.name,'Bentley')

    def test_model(self):
        self.assertEqual(self.car1.model,2022)
        self.assertEqual(self.car2.model,2022)

    def test_color(self):
        self.assertEqual(self.car1.color,'Black')
        self.assertEqual(self.car2.color,'Black')

 

       


    
