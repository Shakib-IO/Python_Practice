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


# 34. Challenge: Reverse Words in a String
S = "Shakib Khan"
ss = ""
SS = S[::-1]
for i in SS:
    if i.islower():
        ss += i.upper()
    else:
        ss += i.lower()
print(ss)

ssd = "".join(map(lambda x: x.upper() if x.lower() else x.lower(), S[::-1]))
print(SSD)

# 56. Solution: Remove Duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
# Using map and lambda to remove duplicates
unique_list = list(map(lambda x: my_list.index(x), sorted(set(my_list), key=my_list.index)))
print(unique_list)

# 74. Solution: Make a Frequency Dictionary from the Elements of a List.
l = [1,1,1,2,3,4,2,3,4,2,3]
dic = {}
for i in range(len(l)):
    if l[i] not in dic:
        dic[l[i]] = 1
    else:
        dic[l[i]] += 1
print(dic)
dict1 = {}
_ = list(map(lambda x: dict1.update({x: dict1.get(x, 0) + 1}), l))
print(dict1)
