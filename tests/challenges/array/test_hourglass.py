from unittest import TestCase

from challenges.array import hourglass


class TestHourglass(TestCase):
    def test_hourglass1(self):
        matrix = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]
        expect = 19
        result = hourglass(matrix)
        self.assertEqual(result, expect)

    def test_hourglass2(self):
        matrix = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 9, 2, -4, -4, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, -1, -2, -4, 0]
        ]
        expect = 13
        result = hourglass(matrix)
        self.assertEqual(result, expect)
