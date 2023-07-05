"""
https://www.studytonight.com/post/python-dataclass-field-function-part-3
Field Function:
This function is used for controlling class attributes present in the dataclass, 
like providing default values, including or excluding any particular attribute 
in __repr__ method, or including/excluding any class attribute in __init__ method 
or not for class objects etc.
"""
"""dataclasses.field(*, default, default_factory, repr, hash, init, compare, metadata)"""
from dataclasses import dataclass, field
import random

"""default Parameter
If no value is specified during the creation of an object in a dataclass for 
a particular class attribute, we can use the field function to provide a default 
value for the class attribute. In the below example, an instance is created and it 
is supplied only one value, whereas the definition of the class has two attributes.
Among these two attributes, one variable has been supplied with a default value using
the field function's default parameter which is used by the newly instantiated object
"""

@dataclass
class Book:
    name: str
    authon: str
    year: str = field(default ="2022")

obj1 = Book("Python Coding Practice", "Van Gough")
print(obj1)

"""default_factory
Using this parameter, we can provide a callable(function etc which returns a value) as 
the default value which acts as a factory method to create a default value for that 
specific class attribute which has the field function with the default_factory parameter. 
If a value is provided to this parameter, it should be a non-zero value that is called when 
a default value is needed.
"""
def generate_amount() -> int: 
    amount = random.randint(10,100)
    return f"${amount}"

@dataclass
class Purchaase:
    name:str
    author: str
    price: int = field(default_factory = generate_amount)

obj2 = Purchaase("Python Coding Practice", "Van Gough")
print(obj2)

"""
init Parameter
repr Parameter
compare Parameter
hash Parameter 
medatadata Parameter: It is usually a key-value pair (a dictionary) that provides the mapping of 
data and more information about the class attribute/field.
"""

@dataclass
class data_class:
    title: str = field(compare = True)
    name: str = field(repr = False)
    language : str = field(default = 'Python3')
    value : int = field(init = False, default = '12')   

class_instance_1 = data_class('Dataclass', 'Studytonight')
class_instance_2 = data_class("Dataclass", "Studytonight")
print(class_instance_1) 
print(class_instance_2) 
print(class_instance_1.value)
print(class_instance_2.name)
print(class_instance_1 != class_instance_2)
