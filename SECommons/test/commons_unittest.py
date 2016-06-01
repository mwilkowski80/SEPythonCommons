import unittest

from SECommons.optional import Optional


def decrement_to_zero_as_None(number):
    number -= 1
    return number if number > 0 else None

class OptionsTest(unittest.TestCase):
    def test_None(self):
        self.assertIsNone(Optional(None).or_else(None))
        self.assertIs('test_None', Optional(None).or_else('test_None'))
        self.assertIsNone(Optional(None).or_else(None))

    def test_simple(self):
        self.assertIs(2, Optional(3).map(decrement_to_zero_as_None)
                      .or_else(-100))
        self.assertIs(1, Optional(3).map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .or_else(-100))
        self.assertIs(-100, Optional(3).map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .or_else(-100))
        self.assertIs(-100, Optional(3).map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .or_else(-100))

    def test_supplier(self):
        self.assertIs(2, Optional(3).map(decrement_to_zero_as_None)
                      .or_else_supplier(lambda: -2))
        self.assertIs(1, Optional(3).map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .or_else_supplier(lambda: -2))
        self.assertIs(-2, Optional(3).map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .or_else_supplier(lambda: -2))
        self.assertIs(-2, Optional(3).map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .map(decrement_to_zero_as_None)
                      .or_else_supplier(lambda: -2))

if __name__ == '__main__':
    unittest.main()
