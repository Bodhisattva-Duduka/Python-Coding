# Write a program using functions to find greatest of three numbers.
def find_greatest(a, b, c):
    if((a>b) and (a>c)):
        return a
    elif((b>a) and (b>c)):
        return b
    elif((c>a) and (c>b)):
        return c
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
greatest_num = find_greatest(a,b,c)
print(f"{greatest_num} is the greatest number")