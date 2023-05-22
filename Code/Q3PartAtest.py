import unittest
from Q3PartA import move_direction

class TestMoveDirection(unittest.TestCase):
    def test_north(self):
        x, y = move_direction('N', 0, 0)
        assert (x, y) == (-1, 0), "north"

    def test_south(self):
        x, y = move_direction('S', 0, 0)
        assert (x, y) == (1, 0), "south"

    def test_east(self):
        x, y = move_direction('E', 0, 0)
        assert (x, y) == (0, 1), "east"

    def test_west(self):
        x, y = move_direction('W', 0, 0)
        assert (x, y) == (0, -1), "west"

    def test_northeast(self):
        x, y = move_direction('NE', 0, 0)
        assert (x, y) == (-1, -1), "northeast"

    def test_northwest(self):
        x, y = move_direction('NW', 0, 0)
        assert (x, y) == (-1, -1), "northwest"

    def test_southeast(self):
        x, y = move_direction('SE', 0, 0)
        assert (x, y) == (1, 1), "southeast"

    def test_southwest(self):
        x, y = move_direction('SW', 0, 0)
        assert (x, y) == (-1, 1), "southwest"

    def test_invalid_direction(self):
        with self.assertRaises(ValueError):
            move_direction('X', 0, 0)

    def test_invalid_xcoord(self):
        with self.assertRaises(ValueError):
            move_direction('N', -1, 0)

    def test_invalid_ycoord(self):
        with self.assertRaises(ValueError):
            move_direction('N', 0, -1)

    def test_invalid_xlimit(self):
        with self.assertRaises(ValueError):
            move_direction('N', 8, 0)

    def test_invalid_ylimit(self):
        with self.assertRaises(ValueError):
            move_direction('N', 0, 8)

if __name__ == '__main__':
    unittest.main()
