from unittest import TestCase

from challenges.array import sort


class TestSort(TestCase):
    def test_sort1(self):
        queue = [4, 3, 1, 2]
        expect = 3
        result = sort(queue)
        self.assertEqual(result, expect)

    def test_sort2(self):
        queue = [2, 3, 4, 1, 5]
        expect = 3
        result = sort(queue)
        self.assertEqual(result, expect)

    def test_sort3(self):
        queue = [2, 3, 4, 1, 5]
        expect = 3
        result = sort(queue)
        self.assertEqual(result, expect)

    def test_sort4(self):
        queue = [3, 7, 6, 9, 1, 8, 10, 4, 2, 5]
        expect = 9
        result = sort(queue)
        self.assertEqual(result, expect)

    def test_sort5(self):
        queue = [
            2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19
        ]
        expect = 46
        result = sort(queue)
        self.assertEqual(result, expect)
