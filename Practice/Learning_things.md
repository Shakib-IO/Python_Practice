- [__post_init__](https://blog.logrocket.com/understanding-python-dataclasses/#:~:text=The%20__post_init__%20method,continent%20%2C%20population%20%2C%20and%20official_lang%20.)
```
The __post_init__ method is called just after initialization.

from dataclasses import dataclass, field

@dataclass
class Country:
     name: str
     population: int
     continent: str = field(repr=False) # Excludes the continent field from string representation
     will_migrate: bool = field(init=False) # Initialize without will_migrate attribute
     official_lang: str = field(default="English") # Sets default language. Attributes with default values must appear last


     def __post_init__(self):
           if self.official_lang == "English":
                 self.will_migrate == True
           else:
                 self.will_migrate == False
```
- [__call__](https://www.geeksforgeeks.org/__call__-in-python/)
```
class Example:
    def __init__(self):
        print("Instance Created")
      
    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")
  
# Instance created
e = Example()
# __call__ method will be called
e()
```
- [super(GCN, self).__init__()](https://realpython.com/python-super/)
- [super()](https://youtu.be/MBbVq_FIYDA)
```
super(): Function used to give access to the methods of a parent class.
          Returns a temporary object of a parent class when used.

super(subclass, self) can also take two parameters: the first is the subclass,
and the second parameter is an object that is an instance of that subclass.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, length):
        super(Square).__init__(length, length)

Here, parent class is Rectangle.
Square class will inherit Rectangle class. By calling the super() method
Square class will get access to the methods of Rectangle.
```
