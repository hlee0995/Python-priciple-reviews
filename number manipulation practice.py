#f srting

#score = 0
#print("Your score is" + score) 
#these line returns an error because it doesn't match the data type 


score = 0
height = 1.8
WInning = True

#f-string
#print(f"Your score is {score}")
#this line works 
#print(f"My score is {score}, my height is{height} and these are all {WInning}")

#Life in Weeks practice


age = input("What is your current age?")

years = 90 - int(age)
month = years * 12
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {month} months left")


