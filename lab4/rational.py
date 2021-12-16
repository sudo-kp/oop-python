from math import gcd, lcm


class Rational:
    """Class for realization of Rational numbers. It has two fields: numerator and denominator.
    Constructor gets two parameters to initialize numerator and denominator. It has properties for getting and setting
    data. The arithmetic and comparison operators are overloaded."""

    def __init__(self, numerator=0, denominator=1):
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        tmp = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // tmp
        self.denominator = denominator // tmp

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, num):
        if not (isinstance(num, int)):
            raise TypeError("Not integer numerator.")
        self.__numerator = num

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denom):
        if not (isinstance(denom, int)):
            raise TypeError("Not integer denominator.")
        if not denom:
            raise ZeroDivisionError("Error.Denominator = 0.")
        self.__denominator = denom

    def __float__(self):
        return self.numerator / self.denominator

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.denominator == other.denominator:
            return Rational(self.numerator + other.numerator, self.denominator)
        tmp = lcm(self.denominator, other.denominator)
        return Rational(self.numerator * tmp // self.denominator + other.numerator * tmp // other.denominator, tmp)

    def __sub__(self, other):
        return self.__add__(-other)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            return NotImplemented
        return self.__mul__(Rational(other.denominator, other.numerator))

    def __eq__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            return NotImplemented
        return (self.numerator, self.denominator) == (other.numerator, other.denominator)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.denominator == other.denominator:
            return self.numerator < other.numerator
        tmp = lcm(self.denominator, other.denominator)
        return self.numerator * tmp // self.denominator < other.numerator * tmp // other.denominator

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        elif not isinstance(other, Rational):
            return NotImplemented
        if self.denominator == other.denominator:
            self.numerator = self.numerator + other.numerator
        tmp = lcm(self.denominator, other.denominator)
        tmp_gcd = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = (self.numerator * tmp // self.denominator +
                          other.numerator * tmp // other.denominator) // tmp_gcd
        self.denominator = tmp // tmp_gcd
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)


def main():
    obj1 = Rational(1, 2)
    print(-obj1)
    obj2 = Rational(2, 3)
    obj3 = Rational(1, 2)
    print(obj1 - obj2)
    print(obj1 * obj2)
    print(obj2 / obj1)
    print(obj1 == obj3)
    print(obj1 <= obj2)
    print(obj1 > obj2)
    print(obj1 >= obj3)
    obj1 += 5
    print(obj1)


if __name__ == '__main__':
    main()
