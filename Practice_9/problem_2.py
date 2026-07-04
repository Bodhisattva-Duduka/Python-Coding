''' The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi score whenever the game() function breaks the Hi-score. '''

def game():
    num = int(input("Enter a number: "))
    return num

a = game()
f = open("Hi-score.txt" , "r")
high_score = int(f.read())
f.close()
if(a>high_score):
    f = open("Hi-score.txt" , "w")
    f.write(str(a))
f.close()

f = open("Hi-score.txt" , "r")
print(f.read())
f.close()






