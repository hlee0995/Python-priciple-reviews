
gun =10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[남은 총] : {0}".format(gun))

def checkpoint_man(gun, soldiers):
    print("gun: {0}\tsoldiers: {1}\t".format(gun,soldiers), end=" ")
    gun = gun - soldiers
    print("남은 총은 {0} 자루 입니다".format(gun))

    return gun 


checkpoint_man(10,5)

#print("{0} 자루가 남았습니다".format(gun))