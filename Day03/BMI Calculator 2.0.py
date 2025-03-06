# Usage of Nested if else ELIF statement!
# By creating  BMI Calculator!
print("Welcome to my BMI Calculator!")
height = float(input("How tall are you? (m) = "))
weight = float(input("What is your weight? (Kg) = "))
bmi = round(weight/(height**2), 1)

if height > 2.72:
    print("are u the tallest person?")
elif bmi < 10:
    print("tui to ekta poka!")
elif bmi < 18.5:
    print(f"your bmi is {bmi} You are underweight, Khawa dawa koren, thik moto!")
elif bmi <= 25:
    print(f"your bmi is {bmi} you have perfect weight")
elif bmi <= 30:
    print(f"your bmi is {bmi} you are over weight")
elif bmi <= 35:
    print(f"your bmi is {bmi} you are obese!!! Appoint a Doctor please")
elif bmi <= 50:
    print(f"Your bmi is {bmi}! Sorry to say, you are clinically obese! Show a Doctor, please! Hope for the best! ")
else:
    print(f"tor bmi {bmi}!shala tui ki manush??")
