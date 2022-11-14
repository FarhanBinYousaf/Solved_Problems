### Find the factorial of given number 
    # Solved 

def FirstFactorial(numbers):
    fact = 1
    for number in range(1,numbers+1):
        fact = fact * number
    return fact
num = int(input())
print(FirstFactorial(num))

# def FirstFactorial(num): 
#     if num == 1:
#         return num
#     else:        
#         factorial = num*FirstFactorial(num-1)    
#         return factorial
    
# # keep this function call here  
# print (FirstFactorial(4))