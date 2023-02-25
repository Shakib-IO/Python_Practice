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


# Another Approach

rev_num = int(str(num)[::-1])

# Compare the original number and the reversed number
if num == rev_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
    
# Exercise 10: Create a new list from a two list using the following condition

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]
print(new_list)

# Exercise 13: Print multiplication table form 1 to 10
for i in range(1,11):
    for j in range(1, 11):
        print(f"{i*j} ", end ="")
    print()

"""
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
"""

"""
I want to build a function that takes as a parameter a list of integers and an integer n
the function should return a list of n lists where each list will store the elements that 
remain after the division with n they have as many positions of the list.
Example:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16]
n = 3
and i want like this:
[[3, 6, 9, 12, 15], [1, 4, 7, 10, 13, 16,],[2, 5, 8, 11, 14]]
"""

for i in range(5):
    for j in range(5, i , -1):
        print("*", end ="")
    print()

    def divi(n:list, nn:int):
    res_list = [[] for i in range(nn)]
    for i, x in enumerate(n):
        res_list[i % nn].append(x)
    return res_list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16]
nn = 3
print(divi(a,nn))


"""
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:
s1 = "America"
s2 = "Japan"

Expected Output:
AraJpn OR AJrpan
"""
s1 = "America"
s2 = "Japan"
strr = ""
ls = [s1, s2]
ld = []


for i in ls:
    print(i)
    middle_value = len(i)//2
    print(middle_value)
    strr = (i[0] + i[middle_value] +i[-1:])
    print(ld.append(strr))

print(ld)
for i in range(len(ld)):
    ld = ''.join(ld)
print(ld)

"""
Given two strings, s1 and s2. Write a program to create a new string 
s3 made of the first char of s1, then the last char of s2, 
Next, the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result
"""
s1 = "Shakib"
s2 = "KHAN"
s2 = s2[: :-1]

s3 = ''
l = min(len(s1), len(s2))
for i in range(l):
    s3 +=(s1[i] + s2[i])

if len(s1) > len(s2):
    s3 += s1[len(s2):]
elif len(s2) > len(s1):
    s3 += s2[len(s1):]
print(s3)

# Exercise 10: Write a program to count occurrences of all characters within a string

str1 = "ShakibKhan"
has = {}
for i in str1.lower():
    cout = str1.count(i)
    has[i] = cout
print(has)

# Exercise 4: Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occ = {}
count = 0

for i in sample_list:
    if i in occ:
        occ[i] +=1
    else:
        occ[i] = 1
print(occ)

# Exercise 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"
len_s = len(str2)
ls = -1 

for i in range(len(str1)):
    if str1[i: i+len_s] == "Emma":
        ls = i
print(ls)

"""
Given two lists, l1 and l2, write a program to create a third list l3 by 
picking an odd-index element from the list l1 and even index elements 
from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
"""
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

for i in range(len(l1)):
    if i%2!=0:
        l3.append(l1[i])
    if i%2==0 and i < len(l2):
        l3.append(l2[i])

print(f"Even & Odd List: {l3}")
for i in range(len(l3)):
    for j in range(i):
        if l3[j] > l3[i]:
            l3[i], l3[j] = l3[j], l3[i]
print(f"Sorted List: {l3}")

# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly", "and", "we"]
list3 = []
l = max(len(list1), len(list2))
for i in range(l):
    if i < len(list1) and i < len(list2):
        list3.append(list1[i] + list2[i])

    elif i < len(list1):
        list3.append(list1[i])
        
    else:
        list3.append(list2[i])

print(list3)
"""
Exercise 5: Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and 
display items from list1 in original order and items from list2 in reverse order.

Given
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:
10 400
20 300
30 200
40 100
"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print(i, j)
# Exercise 7: Add new item to list after a specified item.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

list1[2][2].append(7000)
print(list1)
