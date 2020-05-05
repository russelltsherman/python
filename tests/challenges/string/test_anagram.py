from unittest import TestCase

from challenges.string import anagram


class TestAnagram(TestCase):
    def test_anagram1(self):
        haystack = "BACDGABCDA"
        needle = "ABCD"
        result = anagram(needle, haystack)
        expect = [0, 5, 6]
        self.assertEqual(result, expect)
