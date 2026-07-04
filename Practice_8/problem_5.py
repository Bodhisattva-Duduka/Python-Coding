''' Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

for i in range(0,3):
    for j in range(3-i):
        print("*" , end="")
    print()