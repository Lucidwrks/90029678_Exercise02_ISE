import unittest
from Q3PartA import move_direction

class TestMoveDirection(unittest.TestCase):
    def test_move_direction(self):
        directions = [
            {'Test': 'N', 'x': 0, 'y': 0, 'expected': (0, -1)},
            {'Test': 'S', 'x': 3, 'y': 4, 'expected': (3, 5)},
            {'Test': 'E', 'x': 7, 'y': 2, 'expected': (8, 2)},
            {'Test': 'W', 'x': 5, 'y': 7, 'expected': (4, 7)},
            {'Test': 'NE', 'x': 1, 'y': 1, 'expected': (2, 0)},
            {'Test': 'NW', 'x': 4, 'y': 3, 'expected': (3, 2)},
            {'Test': 'SE', 'x': 6, 'y': 5, 'expected': (7, 6)},
            {'Test': 'SW', 'x': 2, 'y': 6, 'expected': (1, 7)},
            {'Test': 'Invalid', 'x': 0, 'y': 0, 'expected_error': ValueError},

        ]

        for test in directions:
            directions = test['Test']
            x = test['x']
            y = test['y']
            expected = test.get('expected')
            expected_error = test.get('expected_error')

            if expected_error:
                with self.assertRaises(expected_error):
                    move_direction(directions, x, y)
            else:
                result = move_direction(directions, x, y)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
