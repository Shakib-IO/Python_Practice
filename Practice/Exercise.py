# https://pynative.com/python-basic-exercise-for-beginners/

# Exercise 4: Remove first n characters from a string.

s = "Shakib"
new_s = ""
def rm_s(str: s, num:int):
    if num < 0:
        return s
    new_s = s[num:]
    return new_s
print(rm_s(s, 2))        

# Exercise 5: Check if the first and last number of a list is the same

x = [10, 20, 30, 40, 100]

def check_is_same(x:list):
    if x is None:
        return None
    return True if x[0]==x[-1] else False
print(check_is_same(x))
