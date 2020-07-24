import  unittest

from binarySearch import binarySe

class TestExercise(unittest.TestCase):
    def setUp(self):
        pass


    def test_binarycode(self):
        actual = binarySe([1,2,3,4,5,6],0,5,3)
        self.assertEqual(2,actual)

        actual = binarySe([1, 2, 3, 4, 5, 6], 0, 5, 6)
        self.assertEqual(5 , actual)







