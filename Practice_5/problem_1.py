''' Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up! '''
dictionary = {
    "billi" : "cat",
    "kuttha" : "dog",
    "Paani" : "water",
    "khana" : "food"
}
name = input("Enter to the english translation: ")
print(f"English translation is : {dictionary.get(name)}")