''' A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. '''
comment = input("Enter comment here: ")
comment.lower()
money = comment.find("Make a lot of money")
buy = comment.find("buy now")
subscribe = comment.find("subscribe this")
click = comment.find("click this")
if(not(money == -1)):
    print("Its a spam comment")
elif(not(buy == -1)):
    print("Its a spam comment")
elif(not(subscribe == -1)):
    print("Its a spam comment")
elif(not(click == -1)):
    print("Its a spam comment")
else:
    print("It is not a spam comment")
