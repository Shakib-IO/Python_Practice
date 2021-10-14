
#write the function

def isNumber(text):
    if len(text)!= 14:
        return False
    for i in range(0 ,1):
        if text[i] != "+":
            return False
    for i in range(1,3):
        if text[i] != "8":
            return False
    if text[3]!="0":
        return False
    if not text[4:14].isnumeric():
        return False
    
    return True

#Let's write the code and take input from user

input_str = "Please write down my number +8801316195763"
length  = len(input_str)

for i in range(length):
    check = input_str[i:i+14]
    if isNumber(check):
        print("\n\nPhone Number is: " +check)

print("Got your Number!")
