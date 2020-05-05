from unittest import TestCase

from challenges.array import bubbleSort


class TestChallengesArrayBubbleSort(TestCase):
    def test_bubbleSort(self):
        expect = 3
        result = bubbleSort([6, 4, 1])
        self.assertEqual(result, expect)
