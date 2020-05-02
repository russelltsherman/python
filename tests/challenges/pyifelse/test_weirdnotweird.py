from unittest import TestCase

from challenges.pyifelse import is_weird


class TestWeirdNumbers(TestCase):
    def test_oddnum(self):
        expect = "Weird"
        result = is_weird(3)
        self.assertEqual(result, expect)

    def test_evenlow(self):
        expect = "Not Weird"
        result = is_weird(2)
        self.assertEqual(result, expect)

    def test_evenmid(self):
        expect = "Weird"
        result = is_weird(6)
        self.assertEqual(result, expect)

    def test_evenhigh(self):
        expect = "Not Weird"
        result = is_weird(22)
        self.assertEqual(result, expect)
