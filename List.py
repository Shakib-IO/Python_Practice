"""

Question 01: 
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and got a refund of 200$. 
Make a correction to your monthly expense list based on this.
"""

exp = [2200 , 2350 , 2600 , 2130 , 2190]

#1. In Feb, how many dollars you spent extra compare to January?
print(f'In Feb, how many dollars you spent extra compare to January is :' ,exp[1] - exp[0])

#2. Find out your total expense in first quarter (first three months) of the year.
print(f'\nFind out your total expense in first quarter (first three months) of the year is:',exp[0]+exp[1]+exp[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print("\nDid I spent 2000$ in any month? ", 2000 in exp) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("\nExpenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("\nExpenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]


'''
Question 02:
Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function.
'''
print('\n\nPlease Enter the Maximum Number:')
maxnum = int(input())
mylist = []

for i in range(maxnum):
    if i%2==1:
        mylist.append(i)

print('Here is My List:',mylist)