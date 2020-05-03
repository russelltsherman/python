from unittest import TestCase

from challenges.array import chaos


class TestChaos(TestCase):
    def test_chaos1(self):
        queue = [2, 1, 5, 3, 4]
        expect = 3
        result = chaos(queue)
        self.assertEqual(result, expect)

    def test_chaos2(self):
        queue = [5, 1, 2, 3, 7, 8, 6, 4]
        expect = -1
        result = chaos(queue)
        self.assertEqual(result, expect)

    def test_chaos3(self):
        queue = [1, 2, 5, 3, 7, 8, 6, 4]
        expect = 7
        result = chaos(queue)
        self.assertEqual(result, expect)
