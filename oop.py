# oop --> object --> class(written in lower case)
# a class is a blueprint for creating objects
from numbers import result
from strings import name


class Person:
    # constructor function- used to construct/setup a person--> name, age, height etc...
 # constructor setups data
 def __init__(self, name, dob, color, weight, height):
    self.name = name
    self.dob = dob
    self.color = color
    self.weight = weight
    self.height = height
 def display(self):
        print(f"Name is {self.name} and DOB is {self.dob}")

 def get_bmi(self):
     result = self.weight / (self.height * self.height)
     return round(result, 2)

#class name starts with a capital letter, all functions in lower case
p1 = Person("Candy Mwangi", "23-10-2007", "Black", 48.9, 1.43)
p2 = Person("Aisha Juma", "15-01-1980", "Black", 86, 1.86)
p3 = Person("Merlin Goss", "09-07-2000", "White", 65.9, 2.1)

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")
print(f"{p3.name} bmi is {p3.get_bmi()}")