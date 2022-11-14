## 1st from "coderbyte.com"
# Reverse the given string , for example Hello => olleH
        # Solved 

def firstReverse(st):
    NewString = ""
    for string in st:
        NewString = string + NewString
    return NewString
print(firstReverse("Hello World and Coders"))