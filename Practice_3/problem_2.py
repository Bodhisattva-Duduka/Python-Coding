# Write a program to fill in a letter template given below with name and date.
# Template
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
name = input("Enter a name: ")
date = input("Enter date: ")
print(f'''Dear {name}
You are selected! , {date}''')