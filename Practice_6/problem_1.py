# Write a program to find the greatest of four numbers entered by the user.
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))
num_4 = int(input("Enter a number: "))
if((num_1>num_2) and (num_1>num_3) and (num_1>num_4)):
    print(f"{num_1} is the greatest number")
elif((num_2>num_1) and (num_2>num_3) and (num_2>num_4)):
    print(f"{num_2} is the greatest number")
elif((num_3>num_1) and (num_3>num_2) and (num_3>num_4)):
    print(f"{num_3} is the greatest number")
elif((num_4>num_1) and (num_4>num_2) and (num_4>num_3)):
    print(f"{num_4} is the greatest number")
else:
    print("Error has occured")