import math

class Rational:
	def __init__(self, numerator=0, denominator=1):
		if not (isinstance(numerator, int) or isinstance(denominator, int)):
			raise TypeError("Only integers.")
		elif not denominator:
			raise ZeroDivisionError("Error.Denominator = 0.")
		else:
			self.__numerator = numerator//math.gcd(abs(numerator),abs(denominator))
			self.__denominator = denominator//math.gcd(abs(numerator),abs(denominator))

	def __str__(self):
		return f'{self.__numerator}/{self.__denominator}'

	def print_float_format(self):
		print(self.__numerator/self.__denominator)

	def mult(self, multiplier):
		return Rational(self.__numerator*multiplier.__numerator, 
						self.__denominator*multiplier.__denominator)

	def add(self, addend):
		if self.__denominator == addend.__denominator:
			return Rational(self.__numerator+addend.__numerator, self.__denominator)
		return Rational(self.__numerator*addend.__denominator+addend.__numerator*self.__denominator,
						self.__denominator*addend.__denominator)

	def div(self, divisor):
		return self.mult(Rational(divisor.__denominator, divisor.__numerator))

ob = Rational(4, 10)
print(ob)
ob.print_float_format()
print(ob.mult(Rational(8, 10)))
print(ob.add(Rational(-8, 10)))
print(ob.div(Rational(8, 10)))