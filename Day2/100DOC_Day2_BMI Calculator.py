#100DOC - BMI Calculator

height = float(input("What is your height in meters?"))
weight = int(input("What is your weight in kilograms?"))

bmi = weight / height**2

#print("Your BMI is " + str(bmi))

#use an f-string to reduce type conversions

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are considered underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are considered a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are considered slightly overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi} and you are considered overweight")
else:
    print(f"Your BMI is {bmi} and you are considered very overweight")
