from unittest import TestCase

from challenges.array import rotate


class TestRotate(TestCase):
    def test_rotate1(self):
        expect = [5, 1, 2, 3, 4]
        result = rotate([1, 2, 3, 4, 5], 4)
        self.assertEqual(result, expect)

    def test_rotate2(self):
        expect = [1, 2, 3, 4, 5]
        result = rotate([1, 2, 3, 4, 5], 5)
        self.assertEqual(result, expect)
