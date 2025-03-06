print("Welcome to my leap year Detector!")
# A leap year is always divided by 4.
# So I will create a modulas variable.
# First take input.
year = int(input("Enter a year: "))
if year%4 == 0:
    print("This is leap year!")
elif year%100 == 0:
    print("this is leap year")
elif year%400 == 0:
    print("this is leap year")
else:
    print("this is not leap year!")