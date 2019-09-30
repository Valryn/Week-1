class Fraction:
    """
    A simple fraction class

    Attributes:
        numerator(int)
        denominator(int)
    """

    def __init__(self, top, bottom):
        """Constructor checks for integers and auto-reduces"""
        # Check inputs are int
        if isinstance(top, int) and isinstance(bottom, int):
            # Reduce inputs
            common = Fraction.gcd(top, bottom)
            self.numerator = top // common
            self.denominator = bottom // common
        else:
            raise TypeError("Numerator and Denominator must be integers.")

    @property
    def numerator(self):
        """Get and set the numerator"""
        return self.__numerator

    @numerator.setter
    def numerator(self, newnumerator):
        self.__numerator = newnumerator

    @property
    def denominator(self):
        """Get and set the denominator, checking for 0 and correcting negative inputs"""
        return self.__denominator

    @denominator.setter
    def denominator(self, newdenominator):
        # Check for 0 or negative
        if newdenominator > 0:
            self.__denominator = newdenominator
        elif newdenominator < 0:
            # Correct for negative denominator
            self.numerator = self.numerator * -1
            self.denominator = newdenominator * -1
        else:
            raise ValueError("Denominator cannot be 0.")

    @staticmethod
    def reciprocal(fraction):
        """Returns the reciprocal of a fraction"""
        newnumerator = fraction.denominator
        newdenominator = fraction.numerator

        return Fraction(newnumerator, newdenominator)

    @staticmethod
    def gcd(m, n):
        """Returns the greatest common denominator"""
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __str__(self):
        """Returns object as a string"""
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, otherfraction):
        """Defines + operator behavior"""
        newnumerator = self.numerator * otherfraction.denominator + \
                       self.denominator * otherfraction.numerator
        newdenominator = self.denominator * otherfraction.denominator
        return Fraction(newnumerator, newdenominator)

    def __eq__(self, other):
        """Defines == operator behavior"""
        firstnumerator = self.numerator * other.denominator
        secondnumerator = other.numerator * self.denominator

        return firstnumerator == secondnumerator

    def __sub__(self, otherfraction):
        """Defines - operator behavior"""
        newnumerator = self.numerator * otherfraction.denominator - \
                       self.denominator * otherfraction.numerator
        newdenominator = self.denominator * otherfraction.denominator
        return Fraction(newnumerator, newdenominator)

    def __mul__(self, otherfraction):
        """Defines * operator behavior"""
        newnumerator = self.numerator * otherfraction.numerator
        newdenominator = self.denominator * otherfraction.denominator
        return Fraction(newnumerator, newdenominator)

    def __truediv__(self, otherfraction):
        """Defines / operator behavior"""
        return self * Fraction.reciprocal(otherfraction)

    def __gt__(self, otherfraction):
        """Defines > operator behavior"""
        first = self.numerator * otherfraction.denominator
        second = otherfraction.numerator * self.denominator
        return first > second

    def __ge__(self, otherfraction):
        """Defines >= operator behavior"""
        first = self.numerator * otherfraction.denominator
        second = otherfraction.numerator * self.denominator
        return first >= second

    def __lt__(self, otherfraction):
        """Defines < operator behavior"""
        first = self.numerator * otherfraction.denominator
        second = otherfraction.numerator * self.denominator
        return first < second

    def __le__(self, otherfraction):
        """Defines <= operator behavior"""
        first = self.numerator * otherfraction.denominator
        second = otherfraction.numerator * self.denominator
        return first <= second

    def __ne__(self, otherfraction):
        """Defines != operator behavior"""
        first = self.numerator * otherfraction.denominator
        second = otherfraction.numerator * self.denominator
        return first != second

    def __radd__(self, other):
        """Defines + operator behavior when added to other objects
        Fractions can only be added to ints"""
        if type(other) != int:
            raise TypeError()
        else:
            newfraction = Fraction(other, 1)
        return self + newfraction

    def __iadd__(self, otherfraction):
        """Allows Fractions to use the += operator
        Only fractions and ints can be added"""
        return self + otherfraction

    def __repr__(self):
        """Returns identification"""
        return "Fraction(" + str(self.numerator) + ", " + str(self.denominator) + ")"
