from unittest import TestCase

from challenges.array import manipulation


class TestManipulation(TestCase):
    def test_manipulation1(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        expect = 200
        result = manipulation(n, queries)
        self.assertEqual(result, expect)
