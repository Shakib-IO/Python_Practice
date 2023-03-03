# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
ls = dict(zip(keys, values))
print(ls)

# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
ls = {**dict1, **dict2}
# for i, j in zip(dict1, dict2):
#     ls[i], ls[j] = dict1[i], dict2[j]
print(ls)

# Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
# solution
print(sampleDict['class']['student']['marks']['history'])

#Exercise 4: Initialize dictionary with default values
Given:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Output:
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
ls = dict()
for i in range(len(employees)):
    ls[employees[i]] = defaults
print(ls)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
Expected output:
{'name': 'Kelly', 'salary': 8000}
ls = {k: sample_dict[k] for k in keys}
print(ls)

# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}

for x in sample_dict.values():
    if x == 200:
        print(f"{x} is present in the list")
# OR
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print(f"200 is present in the list")
    
# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))

#### Tuple
Exercise 2: Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
    
    
    
    
