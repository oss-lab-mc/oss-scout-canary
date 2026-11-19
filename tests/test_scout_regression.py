import unittest

from counter import format_count


class ScoutRegressionTests(unittest.TestCase):
    def test_one_record_uses_singular(self):
        self.assertEqual(format_count(1), "1 record")
