from gamedata import data
from art1 import logo,vs
import random

print(logo)

list = []
for i in range(1,50):
    list.append(i)
    random.shuffle(list)


def game():
    game = 1
    a=1
    score=0
    while game == 1:
        print(f'Compare A:{data[list[a]]["name"]}, {data[list[a]]["description"]} from {data[list[a]]["country"]}')
        b = data[list[a]]["follower_count"]
        
        print(vs)
        a+=1
        print(f'Compare B:{data[list[a]]["name"]}, {data[list[a]]["description"]} from {data[list[a]]["country"]}')
        c = data[list[a]]["follower_count"]
        
        Answer=input("Who has more followers?")
        if Answer == "A":
            if b > c: 
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score:{score}")
                game = 2
        else:
            if c > b: 
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score:{score}")
                game = 2

game()








    
    



game()



    
    
