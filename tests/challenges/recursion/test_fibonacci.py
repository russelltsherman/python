from unittest import TestCase

from challenges.recursion import fib


class TestChallengesFibonacci(TestCase):
    def test_fibonacci(self):
        expect = 55
        result = fib(10)
        self.assertEqual(result, expect)

        expect = 89
        result = fib(11)
        self.assertEqual(result, expect)

        expect = 377
        result = fib(14)
        self.assertEqual(result, expect)
