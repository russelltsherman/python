from unittest import TestCase

from challenges.pyifelse import hello


class TestChallengeIfElse(TestCase):
    def test_oddnum(self):
        expect = "Weird"
        result = hello(3)
        self.assertEqual(result, expect)

    def test_evenlow(self):
        expect = "Not Weird"
        result = hello(2)
        self.assertEqual(result, expect)

    def test_evenmid(self):
        expect = "Weird"
        result = hello(6)
        self.assertEqual(result, expect)

    def test_evenhigh(self):
        expect = "Not Weird"
        result = hello(22)
        self.assertEqual(result, expect)
