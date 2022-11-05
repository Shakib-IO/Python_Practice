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
