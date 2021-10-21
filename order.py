class Product:
    def __init__(self, name, price=0):
        if price <= 0:
            raise ValueError("Incorrect value of price.")
        # divide type and value error
        if not isinstance(price, (int, float)):
            raise TypeError("Incorrect type of price.")
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, price: {self.price}'


class Customer:
    def __init__(self, name, sname):
        if not isinstance(name, str) or not isinstance(sname, str):
            raise TypeError('Wrong name or surname.')
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
        if not all(isinstance(item, Product) for item in products):
            raise TypeError("Wrong product value for order.")
        self.__customer = customer
        self.__products = products

    def count_value(self):
        value = 0
        for product in self.__products:
            value += product.price
        return value


try:
    products = [Product('apple', 15), Product('pear', 20),
                Product('computer', 1000)]
    for item in products:
        print(item)
    customer = Customer("Eugen", "Petrenko")
    print(customer)
    order = Order(customer, products)
    print(order.count_value())
except ValueError as message:
    print("Wrong value: ", message)
except TypeError as message:
    print("Wrong type: ", message)
except:
    print("Error")
