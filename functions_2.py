def add(a, b, c):
    res = a + b + c
    # a fuction is not supposed to print the answer it should return
    return res

# call the function
print(add(3, 67, 94))


# a function to accept any number of items/arguments
def addition(*nums):
    # documenting functions in python
    """
    Returns the sum of all the numbers passed as arguments
    parameters: integers or floats or a mix of integers and floats
    Returns: sum of numbers inform of integers or floats
    """
    total = sum(nums)
    return total
print(addition(23, 45, 89, 68,15, 36, 90, 34))

# a function to develop a profile of a developer
# kwargs - dictionary - key-word arguments
def build_profile(**kwargs):
    for k, w in kwargs.items():
        print(f"{k} : {w}")
build_profile(experience="2", name="Mercy", age="39")

# function that takes in different types of argument
def fancy_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)

# anonymous functions == lambda functions -functions with no names/ one-line function- have no return keyword
# def square(num):
#     return num * num
# result = square(3)
# print (result)
square = lambda num: num * num
print(square(5))

res = square(98.5)
print(res)

# lambda expression example 2
surface_area_cylinder = lambda r, h: 22/7 * r**2*2 + 22/7 * 2 * r * h
print(surface_area_cylinder(4, 5))

# sorting data in a dictionary
people= [
    {"name": "Mercy", "age": "39"},
    {"name": "Becky", "age": "45"},
    {"name": "George", "age": "89"},
    {"name": "Mary", "age": "46" },
]
# sorted - inbuilt function

sorted_by_age = sorted(people, key= lambda x: x["age"], reverse=True)
print(sorted_by_age)

