# This file for testing the index.py by using Unit Tests
import unittest
from index import calculate_reward

class TestCalculateReward(unittest.TestCase):

    def test_basic_scenario(self):
        events = [("A", 0, 2), ("B", 2, 1), ("A", 10, -1)]
        expected_result = {"A": 5005.556, "B": 4994.444}
        result = calculate_reward(events)
        self.assertEqual(result, expected_result)

    def test_single_user(self):
        events = [("A", 0, 5)]
        expected_result = {"A": 10000.0}
        result = calculate_reward(events)
        self.assertEqual(result, expected_result)

    def test_no_users(self):
        events = []
        expected_result = {}
        result = calculate_reward(events)
        self.assertEqual(result, expected_result)

    def test_negative_adjustments(self):
        events = [("A", 0, 3), ("A", 5, -2), ("A", 10, -1)]
        expected_result = {"A": 10000.0}  # Since A is the only user
        result = calculate_reward(events)
        self.assertEqual(result, expected_result)

    def test_multiple_users(self):
        events = [("A", 0, 2), ("B", 5, 3), ("C", 10, 5)]
        # The expected results would need to be calculated based on the logic of distribute rewards
        expected_result = {"A": 2780.556, "B": 3611.111, "C": 3608.333}
        result = calculate_reward(events)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
