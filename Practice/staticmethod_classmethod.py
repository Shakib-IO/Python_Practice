"""
https://realpython.com/instance-class-and-static-methods-demystified/
@staticmethod
A staticmethod in Python is a method that belongs to a class but does not have access to the class itself (cls) or the instance (self). It's defined using the @staticmethod decorator. The key characteristics of a static method are:

No Access to Instance or Class State: Static methods can't modify object instance state or class state. They are limited to the parameters they receive.
Utility Function: They are often used for utility functions that perform a task in isolation, not depending on class or instance variables.
Called on Class or Instance: Static methods can be called on a class or an instance, but they behave the same in both cases.

class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # Process the arguments
        return arg1 + arg2

result = MyClass.my_static_method(5, 3)
"""
"""
@classmethod
A classmethod, on the other hand, is a method that gets passed the class it's defined on, or a subclass of it, as the first argument instead of the instance of the class. It's defined with the @classmethod decorator. Key points about class methods:

Access to Class State: Class methods can access and modify the class state that applies across all instances of the class.
Factory Methods: Often used as factory methods which can create class instances or static methods that have a logical connection to the class.
First Argument is Class (cls): The first argument to a class method is the class itself, typically named cl

class MyClass:
    @classmethod
    def my_class_method(cls, arg1):
        # Can access class variables and methods via cls
        return cls.some_other_method(arg1)

    @staticmethod
    def some_other_method(arg):
        return arg * 2
"""

"""
Now lets talk about why do we need these methods?

Assuem, we have create a class called Rectangle() and in this class we create an instance method called method() function.
We also have create a classmethod and staticmethod.
So, when we create a class and define an instance method in this class(Everything in python is an object)
"""
class Rectangle:
    def method(self):
        return 'instance method called', self

    @classmethod
    def thisisclassmethod(cls):
        return 'class method called', cls

    @staticmethod
    def thisisstaticmethod():
        return 'static method called'

"""
Now, if we want to access all the method from this class we need to create an object.
obj = Rectangle() # obj is an instance of Rectangle class

Now, what if we don't want to create an object to access these methods.
In that case, the thisisclassmethod and thisisstaticmethod will work fine.(Rectangle.thisisclassmethod() and Rectangle.thisisstaticmethod())
But this Rectangle.method() will raise a typeerror.
"""
#### Without creating any object
print(Rectangle.thisisclassmethod())
# ('class method called', <class '__main__.Rectangle'>)
print(Rectangle.thisisclassmethod())
# static method called
print(Rectangle.method())
# TypeError: method() missing 1 required positional argument: 'self'

#### With creating any object
r = Rectangle()
print(r.thisisclassmethod())
# ('class method called', <class '__main__.Rectangle'>)
print(r.thisisstaticmethod())
# static method called
print(r.method()) 
# ('instance method called', <__main__.Rectangle object at 0x104bbabe0>)
