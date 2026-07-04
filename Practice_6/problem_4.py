''' Write a program to find whether a given username contains less than 10 
characters or not. '''
username = input("Enter a username: ")
length = len(username)
if(length == 10):
    print(f"{username} has 10 characters")
elif(length < 10):
    print(f"{username} has less than 10 characters")
elif(length > 10):
    print(f"{username} has more than 10 characters")