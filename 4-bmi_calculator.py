# take height and weight input

height = float(input("Enter your height in meters: "))

weight = float(input("Enter your weight in kilograms: "))

# check height and weight 

if height <= 0 or weight <= 0:
    print("Invalid input. Height and weight must be greater than 0.")
else:
    bmi = weight / (height * height)

    print("Your BMI is:", round(bmi, 1))

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You are normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")
