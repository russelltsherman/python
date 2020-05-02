from unittest import TestCase

from challenges.recursion import factorial


class TestChallengesFactorial(TestCase):
    def test_factorial(self):
        expect = 3628800
        result = factorial(10)
        self.assertEqual(result, expect)
