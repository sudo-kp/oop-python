from math import gcd


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Only integers.")
        if not denominator:
            raise ZeroDivisionError("Error.Denominator = 0.")
        tmp = gcd(abs(numerator), abs(denominator))
        self.__numerator = numerator // tmp
        self.__denominator = denominator // tmp

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'

    def float_format(self):
        return self.__numerator / self.__denominator

    def mult(self, multiplier):
        if not isinstance(multiplier, Rational):
            raise TypeError('Wrong multiplier.')
        return Rational(self.__numerator * multiplier.__numerator,
                        self.__denominator * multiplier.__denominator)

    def add(self, addend):
        if not isinstance(addend, Rational):
            raise TypeError('Wrong addend.')
        if self.__denominator == addend.__denominator:
            return Rational(self.__numerator + addend.__numerator, self.__denominator)
        return Rational(self.__numerator * addend.__denominator + addend.__numerator * self.__denominator,
                        self.__denominator * addend.__denominator)

    def div(self, divisor):
        if not isinstance(divisor, Rational):
            raise TypeError('Wrong divisor.')
        return self.mult(Rational(divisor.__denominator, divisor.__numerator))


try:
    ob = Rational(4, 10)
    print(ob)
    print(ob.float_format())
    print(ob.mult(Rational(8, 10)))
    print(ob.add(Rational(-8, 10)))
    print(ob.div(Rational(8, 10)))
except TypeError as message:
    print(message)
except ValueError as message:
    print(message)
except:
    print('Error.')