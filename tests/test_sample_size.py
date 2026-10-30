"""
Unit tests for sample size calculator
"""
import unittest
from src.calc_power import calculate_ab_sample_size

class TestSampleSize(unittest.TestCase):
    def test_sample_size(self):
        res = calculate_ab_sample_size(0.05, 0.20, 1000)
        self.assertGreater(res["sample_size_per_variant"], 500)

if __name__ == "__main__":
    unittest.main()
