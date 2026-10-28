# functions methods
from custom_functions import greet

print("Hello World") #built in function

with open("temp.txt", "w") as file:
    file.write("99.34\n")
    file.write("23\n")
    file.write("56.8\n")

with open("temp.txt", "r") as file:
    content = file.read()
    print(content)

greet()