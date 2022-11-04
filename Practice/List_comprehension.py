"""
LIST COMPREHENSION

Conditionals Logic 
new_list = [expression for member in iterable (if conditional)]
"""
# https://blog.devgenius.io/is-list-comprehension-the-most-effective-way-to-solve-any-tasks-python-b6bb3f5391fa

# Use for the questions below:
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."


# Find all of the numbers from 1–1000 that are divisible by 8
q1 = [num for num in nums if num % 8 == 0]
print(q1)

# Find all of the numbers from 1–1000 that have a 6 in them
q2 = [num for num in nums if "6" in str(num)]
print(q2)

# Count the number of spaces in a string (use string above)
q3 = len([space for space in string if space == " "])
print(q3)

# Remove all of the vowels in a string (use string above)
q4 = "".join([char for char in string if char not in ["a", "e", "i", "o","u"]])
print(q4)

# Find all of the words in a string that are less than 5 letters (use string above)
words = string.split(" ")
q5 = [word for word in words if len(word) <5]
print(q5)

# Use a dictionary comprehension to count the length of each word in a sentence (use string above)
q6 ={word:len(word) for word in words}
print(q6)

# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
q7 = [num for num in nums if True in [True for denominator in range(2,10) if num % denominator == 0]]
print(q7)

# For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
q8 = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
print(q8)

"""
MAP()

"""""""
map() function returns a map object (which is an iterator) of the results after 
applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
map(fun, iter)

Example: 
VAT_PERCENT = 0.1  # 10%
def add_vat(price):
    return price + (price * VAT_PERCENT)
    
prices = [10.03, 8.6, 32.85, 41.5, 22.64]

grand_prices = map(add_vat, prices)

print(grand_prices)
grand_prices = list(grand_prices)
print(grand_prices)

OUTPUT: [11.03, 9.46, 36.14, 45.65, 24.9]
"""