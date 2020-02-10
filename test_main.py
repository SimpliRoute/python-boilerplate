from main import sum
import unittest


class TestMain(unittest.TestCase):
    def test_sum_right(self):
        self.assertEqual(sum(2, 9), 11)