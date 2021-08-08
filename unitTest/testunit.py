import unittest

import exam

class TestExam(unittest.TestCase):

    def test_cal(self):

        result= exam.add(3,7)

        self.assertEqual(result,10)
        

    def test_cal1(self):
        result =exam.subsraction(11,7)
        self.assertEqual(result,4)

    def test_cal2(self):
        
        self.assertEqual(exam.subsraction(11,4),7)
        self.assertEqual(exam.add(11,6),17)

    def test_multiply(self):
        self.assertEqual(exam.multiply(2,7),14)
        self.assertEqual(exam.multiply(3,7),21)

    def test_division(self):
        self.assertEqual(exam.divide(12,3),4)

        with self.assertRaises(ValueError):   #context manager
            exam.divide(17,0)
        
        #self.assertRaises(ValueError,exam.divide,17,0)
        

   
        
if __name__ =="__main__":
    unittest.main()