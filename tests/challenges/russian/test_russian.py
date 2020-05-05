
import time
from unittest import TestCase

from challenges.russian import russian
from challenges.russian import caching


class TestRussian(TestCase):
    def test_russian(self):
        expect = 336
        result = russian(16, 21)
        self.assertEqual(result, expect)

    def test_reverse(self):
        expect = 336
        result = russian(21, 16)
        self.assertEqual(result, expect)


class TestCaching(TestCase):
    def test_cached(self):
        start_time = time.time()
        caching(256, 8)
        t1 = time.time()-start_time  # first execution time
        start_time = time.time()
        caching(256, 8)
        t2 = time.time()-start_time  # second execution time
        self.assertGreater(t1, t2, "t2 execution time should be less than t1")
        self.assertGreater(
            t1, (t2*2), "t2 execution time should be less than half t1")
