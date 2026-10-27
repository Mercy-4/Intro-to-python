# if else
import os

name = "Becky"
age = 59

if age > 18:
    print("Adult")
else:
    print("Child")

# inputs - converting str to integer
name = input("Enter your name: ")
age = input("What is your age?")
if not age.isnumeric():
    print("Invalid age")
#     terminate
    os._exit(0)
if int (age) >= 18:
    print(name + "is an adult")
else:
    print(name + "is a child")


