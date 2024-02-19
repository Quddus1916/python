import unittest

from hello import multiply



class MultiplyTestCase(unittest.TestCase):
    def test_multiply_positive_number(self):

        result = multiply(3,4)

        self.assertEqual(result,12)