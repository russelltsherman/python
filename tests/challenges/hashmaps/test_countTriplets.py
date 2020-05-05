from unittest import TestCase

from challenges.hashmaps import countTriplets


class TestChallengesHashmapsCountTriplets(TestCase):

    def test_countTriplets1(self):
        arr = [1, 4, 16, 64]
        r = 4
        expect = 2
        result = countTriplets(arr, r)
        self.assertEqual(result, expect)

    def test_countTriplets2(self):
        arr = [1, 3, 9, 9, 27, 81]
        r = 3
        expect = 6
        result = countTriplets(arr, r)
        self.assertEqual(result, expect)

    def test_countTriplets3(self):
        arr = [1, 5, 5, 25, 125]
        r = 5
        expect = 4
        result = countTriplets(arr, r)
        self.assertEqual(result, expect)
