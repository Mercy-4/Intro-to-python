# bmi calc
# • Underweight: Below 18.5
# • Healthy Weight: 18.5 to 24.9
# • Overweight: 25.0 to 29.9
# • Obesity (Class I): 30.0 to 34.9
# • Obesity (Class II): 35.0 to 39.9
# • Severe Obesity (Class III): 40.0 or higher

weight = input("Enter your weight in Kgs: ")
height = input("Enter your height in M: ")

w = float(weight)
h = float(height)

# h**2 - h to the power of 2, math.power(h,2), h*h
bmi = w / (h ** 2)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi <= 25:
    print("You are healthy")
elif 25.0 <= bmi <= 29.9:
    print("You are Overweight")
elif 30.0 <= bmi <= 34.9:
    print("You are Obese: Class 1")
elif 35.0 <= bmi <= 39.9:
    print("You are Obese: Class 2")
else:
    print("You are obese: Class 3")