from unittest import TestCase

from challenges.string import ransom


class TestRansom(TestCase):
    def test_ransom1(self):
        needle = "give one grand today".split(' ')
        haystack = "give me one grand today night".split(' ')
        result = ransom(haystack, needle)
        expect = "Yes"
        self.assertEqual(result, expect)

    def test_ransom2(self):
        needle = "two times two is four".split(' ')
        haystack = "two times three is not four".split(' ')
        result = ransom(haystack, needle)
        expect = "No"
        self.assertEqual(result, expect)
