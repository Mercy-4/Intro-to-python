#int, float, string

# checking the data type
name = "Meck Candy"
print(name)

print(type(name))

name = 88765
print(name)

print(type(name))

# print name 3 times
name = "Meck Candy"
print(name)
print(name*3)

# adding space between words
f_name = "Meck"
l_name = "Candy"
full_name = f_name +" "+ l_name+ "," +" "+ "This is my name"

print(full_name)
print(full_name.upper())
print(full_name.lower())

f_name_upper = f_name.upper()
print(f_name)

# capitalize function makes only the first letter capital
print("jack jill".capitalize())
# title function capitalizes all first letters of the words
print("jack jill".title())


age = "59"
print(age.isnumeric())