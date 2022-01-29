cabinet = {3:"허준영", 100:"박하은"}
#key = 3, value = 허준영

print(cabinet[3])

print(cabinet.get(3))

#차이점은 위에방법은 키가 없을때는 프로그램을 종료시킨다 하지만 아래방법으로는 키에 해당하는 값이 없을때에는 종료가아닌 
#None 을 리턴한다 

print(cabinet.get(5))
print(cabinet.get(5, "해당값이 없습니다"))
print(3 in cabinet) #true
print(5 in cabinet) #False

pastor = {"1번방":"허준영", "2번방":"박하은"}
print(pastor)
print(pastor.get("1번방"))

pastor["3번방"] = "신민경"
print(pastor)

#덮어쓰기도 가능
pastor["2번방"] = "조세희"
print(pastor)

#값 지우기

del pastor["2번방"]
print(pastor)

#키 값만 출력

print(pastor.keys())
print(pastor.values())
print(pastor.items())

pastor.clear()

print(pastor)

