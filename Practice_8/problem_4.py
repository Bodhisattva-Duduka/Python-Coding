# Write a recursive function to calculate the sum of first n natural numbers.
n = int(input("Enter a number:"))
def sum(n):
    if(n == 1 ):
        return 1
    else:
        return n+sum(n-1) 
    
print(sum(n))