# Calculating Body Mass Index (BMI) and output should be at whole number.
Height = float(input("what is your height (in meter)?= "))        # Type Casting changing input() type string to float, Input Function.
Weight = float(input("What is your weight (in Kg)?="))            # Type Casting changing input()'s type string to float, Input Function.
BMI = int(Weight/Height**2)         # Remember PEDMAS, Making BMI integer because we need output as whole number.
print("Your BMI is= " + str(BMI))       # Changed BMI variable to string for entering string with it, this is called type casting.