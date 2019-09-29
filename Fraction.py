def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        # Reduce inputs
        common = gcd(top, bottom)

        self.numerator = top // common
        self.denominator = bottom // common

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, input):
        # Check for integer.
        if type(input) == int:
            self.__numerator = input
        else:
            raise TypeError("Numerator must be an integer.")

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, input):
        # Check for integer
        if type(input) == int:
            # Check for 0 or negative
            if input > 0:
                self.__denominator = input
            elif input < 0:
                # Correct for negative denominator
                self.numerator = self.numerator * -1
                self.denominator = self.denominator * -1
            else:
                raise ValueError("Denominator cannot be 0.")
        else:
            raise TypeError("Denominator must be an integer.")

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def show(self):
        print(self.numerator, "/", self.denominator)

    def __add__(self, otherfraction):
        newnumerator = self.numerator * otherfraction.denominator + \
                       self.denominator * otherfraction.numerator
        newdenominator = self.denominator * otherfraction.denominator
        return Fraction(newnumerator, newdenominator)

    def __eq__(self, other):
        firstnumerator = self.numerator * other.denominator
        secondnumerator = other.numerator * self.denominator

        return firstnumerator == secondnumerator

    def __sub__(self, otherfraction):
        return self

    def __mul__(self, otherfraction):
        return self

    def __truediv__(self, otherfraction):
        return self

    def __gt__(self, otherfraction):
        return self

    def __ge__(self, otherfraction):
        return self

    def __lt__(self, otherfraction):
        return self

    def __le__(self, otherfraction):
        return self

    def __ne__(self, otherfraction):
        return self

    def __radd__(self, otherfraction):
        return self

    def __iadd__(self, otherfration):
        return self

    def __repr__(self):
        return self

x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
