'''Write a python function to remove a given word from a list ad strip it at the same time.'''

def func(word , l):
    for item in l:
        if(item == word):
            item = l.remove(word)
    return l

word = input("Enter a word: ")
l = ["bodhi" , "aravind" , "akshay" , "akhil"]
list = func(word,l)
print(list)