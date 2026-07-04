''' Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. '''

f = open("poems.txt" , "r")
data = f.read()
if("twinkle" in data):
    print("present")
else:
    print("not present")
