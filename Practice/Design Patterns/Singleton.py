# Singleton.py
# https://refactoring.guru/design-patterns/singleton
# https://python.plainenglish.io/design-patterns-in-python-singleton-5095a4c14f
# https://stackoverflow.com/questions/6760685/what-is-the-best-way-of-implementing-singleton-in-python


# Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.
# Here’s how it works: imagine that you created an object, but after a while decided to create a new one. Instead of receiving a fresh object, you’ll get the one you already created.
# In essence, a Singleton pattern restricts the instantiation of a class to a single object. This means that regardless of how many times the code requests an instance of the class, it will always receive the same instance. 
# Think of it as a gatekeeper for ensuring that a particular class remains unique and unified throughout an application.

"""
All implementations of the Singleton have these two steps in common:
Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
Create a static creation method that acts as a constructor. 
Under the hood, this method calls the private constructor to create an object and saves it in a static field. 
All following calls to this method return the cached object.
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    def log(self, msg):
        print(msg)

obj1 = Logger()
obj2 = Logger()
print("Id of obj1 = {}".format(id(obj1)))
print("Id of obj2 = {}".format(id(obj2)))
print(obj1)
print(obj2)

# Singleton Decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton  # Applying the singleton decorator
class SingletonClass:
    def __init__(self, data):
        self.data = data

    def display(self):
        print(f"Singleton instance with data: {self.data}")


# Creating instances of SingletonClass using the decorator
instance1 = SingletonClass("Instance 1")
instance2 = SingletonClass("Instance 2")

# Both instances will refer to the same instance
instance1.display()  # Output: Singleton instance with data: Instance 1
instance2.display()  # Output: Singleton instance with data: Instance 1

print(id(instance1))
print(id(instance2))
