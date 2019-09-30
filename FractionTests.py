import unittest
import Fraction


class FractionTests(unittest.TestCase):

    def setUp(self):
        self.fraction_x = Fraction.Fraction(1, 2)
        self.fraction_y = Fraction.Fraction(3, 4)

    def test_gcd(self):
        """Returns true if known GCD outcomes are correct"""
        first_case = Fraction.Fraction.gcd(1, 2)
        second_case = Fraction.Fraction.gcd(6, 4)
        third_case = Fraction.Fraction.gcd(578, 9248)

        self.assertEqual(first_case, 1)
        self.assertEqual(second_case, 2)
        self.assertEqual(third_case, 578)

    def test_numerator_setter(self):
        """Returns true if numerator is set correctly"""
        self.fraction_x.numerator = 10
        self.assertEqual(self.fraction_x.numerator, 10)

        self.fraction_x.numerator = 7499291824
        self.assertEqual(self.fraction_x.numerator, 7499291824)

    def test_denominator_setter(self):
        """Returns true if denominator is set correctly, 0 is accounted for, and negatives are corrected"""
        # Check valid denominator
        self.fraction_x.denominator = 10
        self.assertEqual(self.fraction_x.denominator, 10)

        # Check 0
        try:
            self.fraction_x.denominator = 0
        except ValueError:
            self.assertRaises(ValueError)

        # Check negative correction with positive numerator
        self.fraction_x.denominator = -10
        self.assertEqual(self.fraction_x.denominator, 10) and self.fraction_x.numerator < 0

        # Check negative correction with negative numerator
        self.fraction_x.numerator = -1
        self.fraction_x.denominator = -10
        self.assertEqual(self.fraction_x.denominator, 10) and self.fraction_x.numerator < 0

    def test_add(self):
        """Returns true if the "+" operator can be used, and the addition is correct."""
        # Test known outcome (1/2) + (3/4) = (5/4)
        result = self.fraction_x + self.fraction_y
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 4)

    def test_eq(self):
        """Returns true if the "=" operator can be used and the numerators and denominators are equal"""
        first = Fraction.Fraction(1, 2)
        second = Fraction.Fraction(1, 2)

        self.assertEqual(first, second)
        self.assertEqual(first.numerator, second.numerator)
        self.assertEqual(first.denominator, second.denominator)

    def test_sub(self):
        """Returns true if the "-" operator can be used, and the subtraction is correct"""
        # Test known outcome (1/2) - (3/4) = (-1/4)
        result = self.fraction_x - self.fraction_y
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 4)

    def test_mul(self):
        """Returns true if the "*" operator can be used and the multiplication is correct"""
        # Test known outcome (1/2) * (3/4) = (3/8)
        result = self.fraction_x * self.fraction_y
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 8)

    def test_truediv(self):
        """Returns true if the "/" operator can be used and the division is correct"""
        # Test known outcome (1/2) / (3/4) = (2/3)
        result = self.fraction_x / self.fraction_y
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 3)

    def test_gt(self):
        """Returns true if the ">" operator can be used and the comparison is correct"""
        # Test affirmative
        self.assertTrue(self.fraction_y > self.fraction_x)
        # Test negative
        self.assertTrue(not self.fraction_x > self.fraction_y)

    def test_ge(self):
        """Returns true if the ">=" operator can be used and the comparison is correct"""
        # Test affirmative
        self.assertTrue(self.fraction_y >= self.fraction_x)
        # Test negative
        self.assertTrue(not self.fraction_x >= self.fraction_y)
        # Test equal
        new = Fraction.Fraction(1, 2)
        self.assertTrue(self.fraction_x >= new)

    def test_lt(self):
        """Returns true if the "<" operator can be used, and the comparison is correct"""
        # Test affirmative
        self.assertTrue(self.fraction_x < self.fraction_y)
        # Test negative
        self.assertTrue(not self.fraction_y < self.fraction_x)

    def test_le(self):
        """Returns true if the "<=" operator can be used, and the comparison is correct"""
        # Test affirmative
        self.assertTrue(self.fraction_x <= self.fraction_y)
        # Test negative
        self.assertTrue(not self.fraction_y <= self.fraction_x)
        # Test equal
        new = Fraction.Fraction(1, 2)
        self.assertTrue(self.fraction_x <= new)

    def test_ne(self):
        """Returns true if the "!=" comparator can be used and the numerators and denominators are unequal"""
        self.assertNotEqual(self.fraction_x.numerator, self.fraction_y.numerator)
        self.assertNotEqual(self.fraction_x.denominator, self.fraction_y.denominator)

    def test_radd(self):
        """Returns true if a fraction can be added to an integer and return a fraction"""
        correct = Fraction.Fraction(7, 2)
        self.assertEqual(3 + self.fraction_x, correct)

    def test_iadd(self):
        """Returns true if a fraction or int can be added with the "+=" operator"""
        # Test adding a fraction
        self.fraction_x += self.fraction_x
        correct = Fraction.Fraction(1, 1)
        self.assertEqual(self.fraction_x, correct)

        # Test adding an int
        self.fraction_y += 3
        correct = Fraction.Fraction(15, 4)
        self.assertEqual(self.fraction_y, correct)

    def test_repr(self):
        """Returns true if __repr__() returns a string"""
        self.assertTrue(isinstance(self.fraction_x.__repr__(), str))


if __name__ == '__main__':
    unittest.main()
