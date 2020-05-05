from unittest import TestCase

from challenges.hashmaps import sherlockAndAnagrams


class TestChallengesHashmapsSherlockAndAnagrams(TestCase):
    def test_sherlockAndAnagrams1(self):
        needle = "abcd"
        result = sherlockAndAnagrams(needle)
        expect = 0
        self.assertEqual(result, expect)

    def test_sherlockAndAnagrams2(self):
        needle = "abba"
        result = sherlockAndAnagrams(needle)
        expect = 4
        self.assertEqual(result, expect)
