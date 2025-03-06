print("Welcome to my leap year Detector!")
# A leap year is always divided by 4.
# So I will create a modulo variable.
# First take input.
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("This is not leap year!")
