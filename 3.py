'''
3. Паттерн «Фабричный метод»
• Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
• Создайте классы Dog и Cat, которые наследуют от Animal и
реализуют метод speak.
• Создайте класс AnimalFactory, который использует паттерн
«Фабричный метод» для создания экземпляра Animal. Этот
класс должен иметь метод create_animal, который принимает
строку («dog» или «cat») и возвращает соответствующий
объект (Dog или Cat).
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


factory = AnimalFactory()

dog = factory.create_animal("dog")
print(dog.speak())

cat = factory.create_animal("cat")
print(cat.speak())
