import unittest
from Q3PartB import fastest_racer

class TestFastestRacer(unittest.TestCase):
    def test_valid_input_car1_quicker(self):
        winner = fastest_racer("Car1", "Car2", 200, 180, 10, 8)
        self.assertEqual(winner, "Car1")

    def test_valid_input_car2_quicker(self):
        winner = fastest_racer("Car1", "Car2", 290, 310, 12, 15)
        self.assertEqual(winner, "Car2")

    def test_valid_input_tie(self):
        winner = fastest_racer("Car1", "Car2", 268, 268, 12, 12)
        self.assertEqual(winner, "Tie")

    def test_invalid_input_car1_zero_top_speed(self):
        error = fastest_racer("Car1", "Car2", 0, 180, 10, 8)
        self.assertEqual(error, "Invalid Input")

    def test_invalid_input_car2_negative_acceleration(self):
        error = fastest_racer("Car1", "Car2", 260, 220, 10, -8)
        self.assertEqual(error, "Invalid Input")

    def test_invalid_input_both_cars_zero_top_speed(self):
        error = fastest_racer("Car1", "Car2", 0, 0, 10, 15)
        self.assertEqual(error, "Invalid Input")

if __name__ == '__main__':
    unittest.main()
