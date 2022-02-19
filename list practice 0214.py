# Split string method

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#print(names)
def get_numbers(list):
    count = 0;
    for element in list:
        count += 1
    return count

random_factor = get_numbers(names)

print(f"{names[random_factor-1]} is going to buy the meal today")


print(len(names))