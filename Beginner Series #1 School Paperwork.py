# 1st Kata from "codewars.com"

# Q: Your classmates asked you to copy some paperwork for them. 
# You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. 
# If n < 0 or m < 0 return 0.
            # Solved 

def paperwork(n, m):
    if n < 0:
        return 0
    elif m < 0:
        return 0
    else:
        BlankPages = n * m 
        return BlankPages
total = paperwork(5,5)
print(total)