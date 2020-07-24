import  unittest
from reverseIter import ReverseIter
from binarySearch import binarySe


class Testreverselist(unittest.TestCase):
    def setUp(self):
        pass
    def test_reverseList(self):
        r1=ReverseIter([1,2,3,4,5])
        self.assertEqual([5,4,3,2,1],r1.reverseList())

        r1 = ReverseIter([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual([7,6,5,4,3,2,1],r1.reverseList())












if __name__ == '__main__':
    unittest.main()