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

# Exercise 7: Return the count of a given substring from a string

str_x = "Emma is good developer. Emma is a writer and emma can cooked will, also emma loves to read books"
find_s = "Emma"

def find_substring(s, find_s):
    s = s.lower()
    find_s = find_s.lower()
    count = 0
    for i in range(len(s)):
        if s[i:i + len(find_s)] == find_s:
            count +=1
    return count
    
print(find_substring(str_x,find_s))

# Exercise 9: Check Palindrome Number

num = 121
rev_num = 0
temp = num

while temp > 0:
    rev_num = (rev_num * 10) + (temp % 10)
    temp //= 10

if num == rev_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")

