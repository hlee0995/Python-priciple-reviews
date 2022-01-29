#50명의 승객과 매칭 기회가 있을때 총 탑승 승객 수를 구하는 프로그램을 작성하시여

#조건 1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다
#조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.



# create 손님 range, assign 운행시간 , count how many people 
from random import *
#customers=[]
#for customers in range(50):
#    print("{0}번째 손님" + "(소요시간:)" + str(randint(5,50)).format(customers))

total = 0

for i in range(1,51):
    time = randrange(5,51)
    if time <= 15:
        total += 1
    print("{0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {}분".format(total))