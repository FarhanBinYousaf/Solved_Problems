### Q : This kata is about multiplying a given number by eight if it is an even number 
### and by nine otherwise.

def multWithEight(num):
    if num % 2 == 0:
        result = num * 8
    else:
        result = num * 9
    return result
    
mynum = int(input())
print(multWithEight(mynum))