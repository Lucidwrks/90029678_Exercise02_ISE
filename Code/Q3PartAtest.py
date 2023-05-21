import io
import sys
import Q3PartC
import unittest

class TestPieDivider(unittest.TestCase):
    def test_pie_divider(self):
        capout = io.StringIO()
        sys.stdout = capout

        sys.stdin = io.StringIO("2\n5\n") 
        Q3PartC.pie_divider()

        sys.stdout = sys.__stdout__
        output = capout.getvalue()

        expected_output = "2\n1\nPerfect\n" 
        self.assertEqual(output, expected_output)


class TestPieDivider(unittest.TestCase):
    def test_while_loop_perfect(self):
        capout = io.StringIO()
        sys.stdout = capout

        sys.stdin = io.StringIO("-1\n5\n5\n5\n")
        Q3PartC.pie_divider()

        sys.stdout = sys.__stdout__
        output = capout.getvalue()

        expected_output = "Invalid\n5\n5\nPerfect\n"
        self.assertEqual(output, expected_output)

    def test_no_while_loop_perfect(self):
        capout = io.StringIO()
        sys.stdout = capout

        sys.stdin = io.StringIO("5\n5\n")
        Q3PartC.pie_divider()

        sys.stdout = sys.__stdout__
        output = capout.getvalue()

        expected_output = "1\n0\nPerfect\n"
        self.assertEqual(output, expected_output)

    def test_while_loop_not_perfect(self):
        capout = io.StringIO()
        sys.stdout = capout

        sys.stdin = io.StringIO("-1\n5\n2\n")
        Q3PartC.pie_divider()

        sys.stdout = sys.__stdout__

        output = capout.getvalue()

        expected_output = "Invalid\n2\n1\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
