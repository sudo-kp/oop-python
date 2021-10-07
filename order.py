class Product:
	def __init__(self, name, price=0, quantity=1):
		if not isinstance(quantity, int) or quantity<=0:
			raise ValueError("Incorrect value of quantity.")
		if not isinstance(price, (int, float)) or price<=0:
			raise ValueError("Incorrect value of price.")
		self.name = name
		self.price = price
		self.quantity = quantity
	def __str__(self):
		return f'{self.name}, price: {self.price}, {self.quantity} grand'

class Customer:
	def __init__(self, name, sname):
		self.name = name 
		self.sname = sname
	def __str__(self):
		return f'Customer: {self.name} {self.sname}'

class Order:
	def __init__(self, customer, products):
		if not isinstance(customer, Customer):
			raise TypeError("Wrong customer value for order.")
		if not isinstance(products, list):
			raise TypeError("Wrong products type.")
		for item in products:
			if not isinstance(item, Product):
				raise TypeError("Wrong product value for order.")
		self.__customer = customer
		self.__products = products
	def count_value(self):
		value = 0
		for product in self.__products:
			value += product.quantity*product.price
		return value 
try:
	products = [Product('apple', 15, 3), Product('pear', 20, 5), 
				Product('computer', 1000, 1)]
	for item in products:
		print(item)
	customer = Customer("Eugen", "Petrenko")
	print(customer)
	order = Order(customer, products)
	print(order.count_value())
except ValueError:
	print("Wrong value")
except TypeError:
	print("Wrong type")
except:
	print("Error")