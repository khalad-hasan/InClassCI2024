import unittest
from mod2 import substruction as md1


class TestSub(unittest.TestCase):

    def test_substruction(self):
        self.assertEqual(md1(6,3),3)
        self.assertEqual(md1(11,5),6)
     
unittest.main()