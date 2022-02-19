import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
game_images=[rock, paper, scissors]
answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer = random.randint(0,2)
while answer >= 3 or answer < 0:
    print("You entered invalid answer")
    answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
else:
    print(game_images[computer])
    print(game_images[answer])
    while computer == answer:
        print("It's draw\n")
        answer = int(input("Try again! Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
        while answer >= 3 or answer < 0:
            print("You entered invalid answer")
            answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
        computer = random.randint(0,2)
        print(game_images[computer])
        print(game_images[answer])
    if answer == 0 and computer == 2:
        print("You Won")
    elif answer == 2 and computer == 0:
        print("You lost")
    elif answer > computer:
        print("You won")
    elif computer > answer:
        print("You lost")
    # break;
 #   if answer == 0 and computer == 2:
 #       print("You Won")
  #  elif answer == 2 and computer == 0:
   #     print("You lost")
    #elif answer > computer:
     #   print("You won")
    #elif computer > answer:
     #   print("You lost")