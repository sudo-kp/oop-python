class Rectangle:
    def __init__(self, w=1, l=1):
        if not isinstance(w, (int, float)) or not isinstance(l, (int, float)):
            raise TypeError("Wrong length or width.")
        self.__width = w
        self.__length = l

    def set_width(self, wdth):
        if not isinstance(wdth, (int, float)) or not 0 < wdth < 20:
            raise TypeError('Wrong width.')
        if not 0 < wdth < 20:
            raise ValueError('Wrong width value.')
        self.__width = wdth

    def set_length(self, lngth):
        if not isinstance(lngth, (int, float)) or not 0 < lngth < 20:
            raise TypeError('Wrong width.')
        if not 0 < lngth < 20:
            raise ValueError('Wrong length value.')
        self.__length = lngth

    def get_wigth(self):
        return self.__width

    def get_length(self):
        return self.__length

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    def area(self):
        return self.__width * self.__length

try:
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
except ValueError as message:
    print(message)
except TypeError as message:
    print(message)
except:
    print('Error.')


