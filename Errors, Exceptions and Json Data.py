
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
    file.close()
    print("file was closed.")