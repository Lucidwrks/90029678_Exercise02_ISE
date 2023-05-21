import unittest
from Q3PartA import move_direction

class TestMoveDirection(unittest.TestCase):
    def test_valid_direction_north(self):
        x, y = move_direction('N', 0, 0)
        assert (x, y) == (-1, 0), "Failed to move north"

    def test_valid_direction_south(self):
        x, y = move_direction('S', 0, 0)
        assert (x, y) == (1, 0), "Failed to move south"

    def test_valid_direction_east(self):
        x, y = move_direction('E', 0, 0)
        assert (x, y) == (0, 1), "Failed to move east"

    def test_valid_direction_west(self):
        x, y = move_direction('W', 0, 0)
        assert (x, y) == (0, -1), "Failed to move west"

    def test_valid_direction_northeast(self):
        x, y = move_direction('NE', 0, 0)
        assert (x, y) == (-1, -1), "Failed to move northeast"

    def test_valid_direction_northwest(self):
        x, y = move_direction('NW', 0, 0)
        assert (x, y) == (-1, -1), "Failed to move northwest"

    def test_valid_direction_southeast(self):
        x, y = move_direction('SE', 0, 0)
        assert (x, y) == (1, 1), "Failed to move southeast"

    def test_valid_direction_southwest(self):
        x, y = move_direction('SW', 0, 0)
        assert (x, y) == (-1, 1), "Failed to move southwest"

    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            move_direction('X', 0, 0)

    def test_invalid_x_coordinate(self):
        with self.assertRaises(ValueError):
            move_direction('N', -1, 0)

    def test_invalid_y_coordinate(self):
        with self.assertRaises(ValueError):
            move_direction('N', 0, -1)

    def test_invalid_x_upper_bound(self):
        with self.assertRaises(ValueError):
            move_direction('N', 8, 0)

    def test_invalid_y_upper_bound(self):
        with self.assertRaises(ValueError):
            move_direction('N', 0, 8)

if __name__ == '__main__':
    unittest.main()
