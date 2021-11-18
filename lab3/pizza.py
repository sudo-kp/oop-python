from datetime import date
import os.path
import json


class Ingredient:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name == other.name
        raise NotImplementedError

    def __str__(self):
        return f'{self.name}x{self.quantity}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong ingredient type")
        if not name:
            raise ValueError("Empty ingredient name")
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Wrong quantity type")
        if quantity <= 0:
            raise ValueError("Wrong quantity of ingredient or it ran out of it")
        self.__quantity = quantity


class IngredientEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ingredient):
            return obj.name, obj.quantity
        return json.JSONEncoder.default(self, obj)


class Storage:
    def __init__(self, arg):
        self.instock_ingredients = arg
        self.__date = date.today()
        with open("storage.json", 'w') as file:
            json.dump(self.instock_ingredients, file, cls=IngredientEncoder)

    @property
    def instock_ingredients(self):
        return self.__instock_ingredients

    @instock_ingredients.setter
    def instock_ingredients(self, ingred):
        if isinstance(ingred, str):
            if not os.path.exists(ingred):
                raise ValueError("File doesn't exist")
            with open(ingred, 'r') as file:
                ingrdts = json.load(file)
            ingr = []
            for item in ingrdts:
                ingr.append(Ingredient(item[0], item[1]))
            if not isinstance(ingr, list):
                raise TypeError()
            if not ingr:
                raise ValueError("Empty ingredients")
            if not all(isinstance(entry, Ingredient) for entry in ingr):
                raise TypeError()
            self.__instock_ingredients = ingr
        elif isinstance(ingred, list):
            if not ingred:
                raise ValueError("Empty ingredient list")
            if not all(isinstance(entry, Ingredient) for entry in ingred):
                raise TypeError("Not ingredient in ingredient list")
            self.__instock_ingredients = ingred
        else:
            raise TypeError()


def factory():
    match date.today().weekday():
        case 0:
            return PizzaOfTheMonday
        case 1:
            return PizzaOfTheTuesday
        case 2:
            return PizzaOfTheWednesday
        case 3:
            return PizzaOfTheThursday
        case 4:
            return PizzaOfTheFriday
        case 5:
            return PizzaOfTheSaturday
        case 6:
            return PizzaOfTheSunday


class PizzaOfTheDay:
    storage = None
    price = 0
    pizza_ingredients = []

    def __init__(self, extra_ingred, size):
        if not isinstance(self.storage, Storage):
            raise TypeError("Storage is not defined.")
        if not self.pizza_ingredients:
            raise ValueError("Pizza ingredients are not defined")
        if not isinstance(self.pizza_ingredients, list):
            raise TypeError("Wrong pizza ingredients list")
        if not all(isinstance(pizza_ingredient, Ingredient) for pizza_ingredient in self.pizza_ingredients):
            raise TypeError("Wrong pizza ingredient type")
        if not all(pizza_ingredient in self.storage.instock_ingredients for pizza_ingredient in self.pizza_ingredients):
            raise ValueError("No such ingredient")
        inst_ingr = self.storage.instock_ingredients
        for pizza_ingredient in self.pizza_ingredients:
            inst_ingr[inst_ingr.index(pizza_ingredient)].quantity -= pizza_ingredient.quantity
        self.extra_ingredients = extra_ingred
        self.size = size
        with open("storage.json", 'w') as file:
            json.dump(self.storage.instock_ingredients, file, cls=IngredientEncoder)

    @property
    def extra_ingredients(self, ):
        return self.__extra_ingredients

    @extra_ingredients.setter
    def extra_ingredients(self, extra_ingred):
        if not isinstance(extra_ingred, list):
            raise TypeError("Wrong extra ingredients")
        if not all(ingredient in self.storage.instock_ingredients for ingredient in extra_ingred):
            raise ValueError("No such ingredient")
        inst_ingr = self.storage.instock_ingredients
        for extra_ingredient in extra_ingred:
            inst_ingr[inst_ingr.index(extra_ingredient)].quantity -= extra_ingredient.quantity

        self.__extra_ingredients = extra_ingred

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not (size in (30, 60, 90)):
            raise ValueError("Wrong pizza size")
        self.__size = size

    def __str__(self):
        a = []
        for item in self.pizza_ingredients:
            a.append(str(item))
        b = []
        for item in self.extra_ingredients:
            b.append(str(item))
        return f"Pizza: {a} with extra {b}, size: {self.size}"


class PizzaOfTheMonday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class PizzaOfTheTuesday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class PizzaOfTheWednesday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class PizzaOfTheThursday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class PizzaOfTheFriday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class PizzaOfTheSaturday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class PizzaOfTheSunday(PizzaOfTheDay):
    storage = None
    price = 0
    pizza_ingredients = []


class Cart:
    def __init__(self, items):
        if not isinstance(items, list|tuple):
            raise TypeError()
        if not all(isinstance(item, factory()) for item in items):
            raise TypeError()
        self.items = items

    def __str__(self):
        a = []
        for item in self.items:
            a.append(str(item))
        return f'{a}'


o = Storage("storage.json")
print(*o.instock_ingredients)
PizzaOfTheDay.pizza_ingredients = [Ingredient('sausage', 20), Ingredient('tomato', 10)]
PizzaOfTheDay.storage = o
classname = factory()
classname.storage = o
classname.pizza_ingredients = [Ingredient('chicken', 5), Ingredient('pineapple', 2)]
obj1 = classname([Ingredient('mushroom', 10)], 30)
print(obj1)
obj2 = classname([], 60)
cart = Cart((obj1, obj2))
print(cart)
