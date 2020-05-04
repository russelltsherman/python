from unittest import TestCase

from challenges.array import common


class TestCommon(TestCase):
    def test_common1(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = common(a, b)
        self.assertEqual(result, expect)

    def test_common2(self):
        a = [1, 5, 15, 20, 30, 37]
        b = [2, 5, 13, 30, 32, 35, 37, 42]
        expect = [5, 30, 37]
        result = common(a, b)
        self.assertEqual(result, expect)

    def test_common3(self):
        a = [1, 6, 15, 20, 31, 45]
        b = [2, 5, 13, 30, 32, 35, 37, 42]
        expect = []
        result = common(a, b)
        self.assertEqual(result, expect)
