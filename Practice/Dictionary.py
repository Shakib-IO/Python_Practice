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
