# https://refactoring.guru/design-patterns/abstract-factory
# https://medium.com/@amirm.lavasani/design-patterns-in-python-factory-method-1882d9a06cb4
# https://python-patterns.guide/gang-of-four/abstract-factory/
# Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.


from abc import abstractmethod, ABC

"""
We start by defining the Product, which is the abstract class representing translations. 
Each translation will have a common interface with a method called localize. Next, 
we create Concrete Products, which are the translations for specific languages. 
We will create three concrete translation classes, one for each language: French, English, and Spanish.
"""
class Product(ABC):
    @abstractmethod
    def localize(self, msg):
        """Translate the message"""
        pass
    

class FrenchLocalizer(Product):
    """A concrete product which creates
    French translations"""

    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }
    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer(Product):
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }
    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer(Product):
    def localize(self, msg):
        return msg
    

message = ["car", "bike", "cycle"]
f = FrenchLocalizer()
s = SpanishLocalizer()
e = EnglishLocalizer()
for i in range(len(message)):
    print(f"{message[i]} in French: {f.localize(message[i])}")
    print(f"{message[i]} in Spanish: {s.localize(message[i])}")
    print(f"{message[i]} in English: {e.localize(message[i])}")
    print("\n")
