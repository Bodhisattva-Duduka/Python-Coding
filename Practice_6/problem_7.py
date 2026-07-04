''' Write a program to find out whether a given post is talking about “Harry” or not. '''
text = input("Enter a statement: ")
str = text.lower()
if("harry" in str):
    print("It is talking about Harry")
else:
    print("It is not talking about Harry")