# Write a python program using function to convert Celsius to Fahrenheit.

def convert(celsius):
    fahrenheit = (celsius*(9/5))+32
    return fahrenheit

c = int(input("Enter value here: "))
fahrenheit = convert(c)
print(fahrenheit)


