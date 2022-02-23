#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#print(chosen_word)

#print(len(chosen_word))

answer = list(chosen_word)

guess_this =[]

for i in range(len(chosen_word)):
    #guess_this.append(["_"])
    guess_this += "_"

print(guess_this)



#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while "_" in guess_this: 
    guess = input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
       letter = chosen_word[position]
       if letter == guess:
          guess_this[position] = letter
    print(guess_this)
print("You win!")

print(guess_this)


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
