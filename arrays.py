ages = [21, 72, 43, 59, 28, 39, 37, 40]  # list/array
names = ["Becky", "Mary", "Kamaa", "Meck"]

# list functions
ages.append(45)  # append function is used to add to the list
# ages.clear()
# ages.sort() #arranges numbers is ascending order
# ages.reverse() #arranges to descending order

print(ages)

# arrange names in ascending order
# names.sort()

# arrange in reverse order
# names.sort(reverse=True)
print(names)

becky_count = names.count("Becky")
print(becky_count)

# counting number of items on the list
print(len(names))
print(len(ages))

# calculating the sum of the ages
print(sum(ages))

# calculating the average
print(sum(ages) / len(ages))

# function to retrieve an element from the list/index
print(ages[0])
print(ages[7])
print(names[0])

# start counting from the end (python specific)
print(names[-1])
print(names[-3])

# slicing the list from the end
print(names[-3:])

# slicing from the beginning from the specified index to the end
print(ages[3:])

# slicing from index 3 to 5 but 5 is not included
print(ages[3:5])

# slicing from index 0 to 3 but 3 is not included
print(ages[0:3])

# set - everything only exists once- removes duplicates when printing
scores = {34, 67, 59, 23, 39, 17, 59}
print(scores)

# tuple- does not allow addition of more elements/ can't be modified/ immutable
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays)
print(weekdays[4])

# dictionary - has keywords with meaning
person = {"name": "Abby", "age": 8, "city": "Nairobi", "height": "80 cm", "weight": 23}
print(person["name"])
print(person["age"])
print(person["height"])

# list of dictionaries
people = [
    {"name": "Merlin", "age": 40, "city": "Dublin"},
    {"name": "Mike", "age": 38, "city": "Nairobi"},
    {"name": "Liam", "age": 1, "city": "Mombasa"}
]
print(people[0]["age"])