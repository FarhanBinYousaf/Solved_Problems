# 2nd form "codewars.com"
# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
        # Solved 

        
def abbrev_name(name):
    abbrevatedName = []
    splitedName = name.split()
    for i in splitedName:
        abbrevatedName.append(i[0])
    return '.'.join(abbrevatedName).upper()
print(abbrev_name("Sam Harris"))




# string = "hello World"
# newString = []
# name = string.split()
# for n in name:
#     newString.append(n[0])
# print ('.'.join(newString).upper())