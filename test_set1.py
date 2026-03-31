import unittest
from questions_set1 import *

class TestSetOne(unittest.TestCase):

    def test_even_odd_tracker(self):
        self.assertEqual(
            even_odd_tracker([1, 2, 3, 4]),
            ["Odd", "Even", "Odd", "Even"]
        )

    def test_temperature_filter(self):
        self.assertEqual(
            temperature_filter([10, 18, 22, 30, 61, -100]),
            [18, 22]
        )

    def test_calculate_order_total(self):
        self.assertEqual(calculate_order_total(5, 2), 50)
        self.assertEqual(calculate_order_total(5, 6), 10 + (5*6) + 20)

    def test_process_scores(self):
        self.assertEqual(
            process_scores([60, 70, 35, 80]),
            "Stopped early at score 35"
        )
        self.assertEqual(
            process_scores([45, 50, 55]),
            "All scores processed"
        )

    def test_organize_products(self):
        data = [
            {"name": "Milk", "category": "Dairy"},
            {"name": "Cheese", "category": "Dairy"},
            {"name": "Bread", "category": "Bakery"}
        ]
        expected = {
            "Dairy": ["Milk", "Cheese"],
            "Bakery": ["Bread"]
        }
        self.assertEqual(organize_products(data), expected)

    def test_sequence_growth(self):
        self.assertEqual(sequence_growth([3, 4, 5, 1, 2]), 3)
        self.assertEqual(sequence_growth([1, 2, 3, 4, 5]), 5)
        self.assertEqual(sequence_growth([5, 4, 3, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
