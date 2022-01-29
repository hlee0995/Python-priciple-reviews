#당신의 학교에서는 파이썬 코딩대회를 주최합니다.
#참석률을 높이기 위해 댓글 이벤트를 합니다
#댓글 작성자들 중에 추첨을 토앻 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#추첨 프로그램을 작성하시요 

#조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
#조건 2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
#조건 3: random 모듈의 shuffle과 sample 을 활용 

#출력예제 
#-- 당첨자 발표 -- 
#치킨 당첨자 : 1
#커피 당첨자: [2,3,4]
#-- 축하합니다 -- 

from random import * 

i = 0 
후보자 = []

while i < 20:
    후보자.append(i)
    i += 1

print(후보자)

shuffle(후보자)

print(후보자)


print("치킨 당첨자: " + str(후보자[0]) + "\n")
print("커피 당첨자: " + str(후보자[1]),str(후보자[2]),str(후보자[3]) + "\n")
print("식사 당첨자: " + str(sample(후보자,3)) + "\n")
print("-- 축하합니다 -- ")

#2번째 방법

from random import *

users = range(1,21)
print(type(users)) #class 가 range 인것을 확인
users = list(users)
print(type(users))

shuffle(users)
print(users)

winners = sample(users, 4)

print(" ---  당첨자 발표 --- \n")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:4]))
print("\n ---  축하합니다 --- \n")
