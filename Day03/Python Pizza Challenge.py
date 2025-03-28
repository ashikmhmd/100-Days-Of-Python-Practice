# I have to make an order program for a company name Python Pizza!
# They have three types of pizza small, medium,  large.
# The price is 15$, 20$, 25$ corresponding.
# Customer can add pepperoni for small pizza at 2$ and 3$ for medium and large pizza.
# Extra cheese for any pizza is 1$.
print("Welcome to Python Pizza!")
pizza = str(input("Which Pizza do you want? [s/m/l]? = "))
pepperoni = str(input("Do you want any pepperoni? [y/n]? = "))
cheese = str(input("Do you want extra cheese? [y/n] ="))
bill = 0
if pizza == "s":
    bill += 15
elif pizza == "m":
    bill += 20
elif pizza == "l":
    bill += 25
if pepperoni == "y":
    if pizza == "s":
        bill += 2
    else:
        bill += 3

if cheese == "y":
    bill += 1
print(f"your total bill is ${bill}")