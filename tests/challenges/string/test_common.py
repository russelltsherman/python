from unittest import TestCase

from challenges.string import common


class TestCommon(TestCase):
    def test_common1(self):
        needle = "hello"
        haystack = "world"
        result = common(needle, haystack)
        expect = "YES"
        self.assertEqual(result, expect)

    def test_common2(self):
        needle = "hi"
        haystack = "world"
        result = common(needle, haystack)
        expect = "NO"
        self.assertEqual(result, expect)
