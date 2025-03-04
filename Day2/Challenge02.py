# Need to find How many days, weeks and months user has left! ( In a funny way)
# First we need know the age of user!
age = int(input("what is your age? = "))
live = int(input("In what age you want to die? = "))
# Find out total years he wants to live!
years = live - age
months = years*12
weeks = years*52
Days = years*365
print(f"You have left {years} years, {months} months, {Days} days! "
      f"Comrade! Long Live! The World is a BattleGround! And you are still Alive! Congo!")

