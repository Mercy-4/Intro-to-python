def greet():
    print("Hello")


#     empty brackets- the function has no parameters/arguments
greet()


def greeting(name):
    print(f"Hello {name}")


greeting('xcvfgbn')
greeting('xcvfgbn')
greeting('xcvfgbn')


def volume_cylinder(radius, height):
    v = 22 / 7 * radius ** 2 * height
    print(round(v, 2))


volume_cylinder(5, 12)


# return command
def volume_cylinder2(radius, height):
    v = 22 / 7 * radius ** 2 * height
    return v


result = volume_cylinder2(7.2, 90)
print(round(result, 2))
# saving the answer to a text file  called volume.txt instead of printing out the result
with open("volume.txt", "w") as file:
    file.write(str(result))


# use the specified order to pass the parameters- insert radius then height
def volume_surface(radius, height):
    v = 22 / 7 * radius ** 2 * height
    a = 22 / 7 * radius ** 2 * 2 + 22 / 7 * radius * 2 * height
    return v, a


volume, area = volume_surface(6, 18)
print(f"volume is {volume} and area is {area}")

# named parameters to be flexible with the order you pass the parameters
v, a = volume_surface(height=20, radius=5)
print(f"volume is {v} and area is {a}")


def divide(x, y, should_round= False):
    res = x / y
    if should_round == True:
        return round(res, 2)
    else:
        return res

print(divide(25, 2.6, should_round=True))
