import unittest

from maths import sqrt
from parameterized import parameterized


class SquareRootTest(unittest.TestCase):
    @parameterized.expand(
        [(0,),
         (1,),
         (4,),
         (9,),
         (16,),
         (0.25,),
         (25,)]
    )
    def test_square_root(self, input):
        self.assertEqual(input, sqrt(input) * sqrt(input))


if __name__ == '__main__':
    unittest.main()
