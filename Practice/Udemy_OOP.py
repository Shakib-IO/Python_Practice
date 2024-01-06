"""Inheritance"""
# Parent Class
class Employee:
  
    salary = 100000
    monthly_bonus = 500
 
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
 
# Inherits from Employee
class Programmer(Employee):
  
    def __init__(self, name, age, address, phone, programming_languages):
        Employee.__init__(self, name, age, address, phone)
        self.programming_languages = programming_languages 
 
# Inherits from Employee
class Assistant(Employee):
  
    def __init__(self, name, age, address, phone, bilingual):
        Employee.__init__(self, name, age, address, phone)
        self.bilingual = bilingual
        
# Instances
programmer = Programmer("Isabel", 45, "5th avenue", "556-345-543", ["Java"])
assistant = Assistant("Jack", 18, "6th avenue", "452-355-234", True)
 
# Instance attributes
print(programmer.name)
print(assistant.age)
 
# Class attributes
print(programmer.salary)
print(assistant.monthly_bonus)

"""Coding Practice"""
# 28. Problem: Remove Spaces from a String.
s = "The quick brown fox jumped over the lazy dog."
ss = ""
for i in s:
    if i != " ":
        ss += i
print(ss)
# Using Lambda and Map function
print(''.join(map(lambda x: x if x != " " else "", s)))

