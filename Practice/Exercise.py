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
