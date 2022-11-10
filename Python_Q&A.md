```
So by doing x=x[:,1] we get all the rows in x present at index 1.
x = array([
   [0.69859393, 0.1042432 ],
   [0.55138493, 0.18639614],
   [0.27338772, 0.80351282]
   ])
x[:,1] = array([0.1042432 , 0.18639614, 0.80351282])
```

```
# Single selections using iloc and DataFrame
# Rows:
data.iloc[0] # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
data.iloc[1] # second row of data frame (Evan Zigomalas)
data.iloc[-1] # last row of data frame (Mi Richan)
# Columns:
data.iloc[:,0] # first column of data frame (first_name)
data.iloc[:,1] # second column of data frame (last_name)
data.iloc[:,-1] # last column of data frame (id)
```
```
[Role of Underscore(_) in Python Tutorial](https://www.datacamp.com/tutorial/role-underscore-python)
1. Python automatically stores the value of the last expression in the interpreter to a particular variable called "_." You can also assign these value to another variable if you want.
2. Underscore(_) is also used to ignore the values. If you don't want to use specific values while unpacking, just assign that value to underscore(_).
3. You can use underscore(_) as a variable in looping. See the examples below to get an idea.
4. If you have a long digits number, you can separate the group of digits as you like for better understanding.
```
```
Python Decorators Tutorial: https://www.datacamp.com/tutorial/decorators-python

```
