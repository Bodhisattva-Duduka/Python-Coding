''' Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. '''
maths = float(input("Enter the marks: "))
science = float(input("Enter the marks: "))
english = float(input("Enter the marks: "))
b = ((maths + science + english)*(40/100))
if((maths< 33) or (science< 33) or (english< 33)):
    print("Failed")
elif(b<40):
    print("Failed")
else:
    print("Passed")