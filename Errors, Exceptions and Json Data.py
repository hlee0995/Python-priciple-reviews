
#Case1 :
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")
    file.write("something")

#Case 2:

try:
    file = open("a_file.txt")
    #a_dictionary = {"key": "Value"}
    #print(a_dictionary["non-key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else: 
    content = file.read()
    print(content)
finally:
    raise TypeError("This is the error")

#Case 3 

height = float(input("Your height: "))
weight = float(input("your weight: "))

if height > 3:
    raise ValueError("HumAN Height should not be oevr 3 meters")

bmi = weight / height ** 2
