# What is Dependency Injection?
# https://youtu.be/fhwhQjY2GCY
"""
In simpler terms, it's about providing objects with the things they need to function, rather than making them create those things themselves.

Here's a breakdown of the concept:
Dependency: An object relies on another object (or service) to perform its tasks. This "other object" is considered a dependency.
Injection: Instead of creating its dependencies internally, an object receives them from external code. This "external code" is often called an injector.

"""
# Example:

### BEFORE
from dataclasses import dataclass
@dataclass
class User:
  name: str
  age: int

def do_something():
  user = User(name = "Shakib", age = 27)
  print(user)

# Now the problem with this code is, If I want to create a new user than I need to define it again in the do_something function.
def main():
  do_something()

if __name__ == "__main__":
  main()

### AFTER apply dependency injections
from dataclasses import dataclass
@dataclass
class User:
  name: str
  age: int

def do_something(user:User):
  user.age += 1
  print(user)

# Now the problem with this code is, If I want to create a new user than I need to define it again in the do_something function.
def main():
  user = User(name = "Shakib", age = 27)
  do_something(user)
  user2 = User(name = "Hasib", age = 24)
  do_something(user)

if __name__ == "__main__":
  main()
