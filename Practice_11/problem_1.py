''' Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’. '''

class Animals:
    def makeSound(self):
        print("animal is making sound")

class Pets(Animals):
    def bark(self):
        print("dog is barking")
    
class Dog(Pets):
    print("Dog is a animal")

obj = Dog()
print(obj.bark())