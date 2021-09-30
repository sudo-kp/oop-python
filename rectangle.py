class Rectangle:
	def __init__(self):
		self.__width = 1
		self.__length = 1

	def set_width(self, wdth):
		if (type(wdth)==int or type(wdth)==float) and wdth<20 and wdth>0:
			self.__width = wdth

	def set_length(self, lngth):
		if (type(lngth)==int or type(lngth)==float) and lngth<20 and lngth>0:
			self.__length = lngth

	def get_wigth(self):
		return self.__width

	def get_length(self):
		return self.__length

	def perimeter(self):
		return 2*(self.__width+self.__length)

	def area(self):
		return self.__width*self.__length

rect1 = Rectangle()
print(rect1.get_length(), ' ', rect1.get_wigth())

rect1.set_width(5)
rect1.set_length(8)
print(rect1.get_length(), ' ', rect1.get_wigth())

rect1.set_width(-5)
rect1.set_length('8')
print(rect1.get_length(), ' ', rect1.get_wigth())

print(rect1.area())
print(rect1.perimeter())