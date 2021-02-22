height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

# calculate the BMI
bmi = round(weight / height ** 2, 2)

# tell the user which category he/she belongs
if (bmi < 18.5):
    print(f"Your BMI is: {bmi} and you are underweight.")
elif (bmi > 18.5 and bmi < 25):
    print(f"Your BMI is: {bmi} and you are normal weight.")
elif (bmi > 25 and bmi < 30):
    print(f"Your BMI is: {bmi} and you are overweight.")
elif (bmi > 30 and bmi < 35):
    print(f"Your BMI is: {bmi} and you are obese.")
else:
    print(f"Your BMI is: {bmi} and you are clinically obese.")