import unittest

from simplecurry import curried

@curried
def add(x, y, z):
    return x + y + z

class TestCurry(unittest.TestCase):
    def test_one_parameter(self):
        assert callable(add(1))

    def test_two_parameters(self):
        assert callable(add(1, 2))
        assert callable(add(1)(2))

    def test_three_parameters(self):
        assert add(1, 2, 3) == 6
        
    def test_grouping_one(self):
        assert add(1)(2, 3) == 6

    def test_grouping_two(self):
        assert add(1, 2)(3) == 6
