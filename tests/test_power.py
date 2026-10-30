"""
Unit tests for CRO Power Calculator
"""
import unittest
from src.calc_power import calculate_ab_sample_size

class TestCROPower(unittest.TestCase):
    def test_sample_size_calculation(self):
        res = calculate_ab_sample_size(0.05, 0.20, 1000)
        self.assertGreater(res["sample_size_per_variant"], 1000)
        self.assertGreater(res["estimated_duration_days"], 0)
        self.assertEqual(res["feasibility"], "FEASIBLE")

if __name__ == "__main__":
    unittest.main()
