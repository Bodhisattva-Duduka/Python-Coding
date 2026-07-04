# Write a program to find whether a given number is prime or not.
num = int(input("Enter a number(only positive numbers): "))
i = 1
while(num>0):
    if(num == 1):
        print("It is neither prime not composite1")
    elif((num % i == 0) and (not(i == 1) and not(i == num))):
        print("It is not a prime number")
        break
    elif(i>num):
        print("It is a prime number")
        break
    i += 1