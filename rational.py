
def greatest_common_divisor(numerator, denominator):
	while numerator!=denominator:
		if numerator>denominator:
			numerator -= denominator
		else:
			denominator -= numerator
    return numerator

class Rational:
	def __init__(self, numerator=0, denominator=1):
		if type(numerator)!=int or type(denominator)!=int:
			raise TypeError("Only integers.")
		elif not denominator:
			raise ZeroDivisionError("Error.Denominator = 0.")
		else:
			self.__numerator = numerator/greatest_common_divisor(abs(numerator),abs(denominator))
			self.__denominator = denominator/greatest_common_divisor(abs(numerator),abs(denominator))
	
