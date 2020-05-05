from unittest import TestCase

from challenges.hashmaps import frequencyQuery


class TestChallengesHashmapsFrequencyQuery(TestCase):
    def test_frequencyQuery(self):
        arr = [[1, 5], [1, 6], [3, 2], [1, 10],
               [1, 10], [1, 6], [2, 5], [3, 2]]
        expect = [0, 1]
        result = frequencyQuery(arr)
        self.assertEqual(result, expect)
