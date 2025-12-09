'''
2. Паттерн «Строитель»
• Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions, bacon.
• Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
• Создайте класс PizzaDirector, который принимает экземпляр
PizzaBuilder и содержит метод make_pizza, который
использует PizzaBuilder для создания Pizza.
'''

class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False,
                 mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = []
        if self.cheese: toppings.append("cheese")
        if self.pepperoni: toppings.append("pepperoni")
        if self.mushrooms: toppings.append("mushrooms")
        if self.onions: toppings.append("onions")
        if self.bacon: toppings.append("bacon")

        return f"Pizza(size={self.size}, toppings={', '.join(toppings) if toppings else 'none'})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder
                .set_size("Large")
                .add_cheese()
                .add_pepperoni()
                .add_bacon()
                .build())


builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)