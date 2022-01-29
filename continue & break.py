#absent = [2,5] # 결석
#no_book=[7]

#for student in range (1,11):
 #   if student in absent:
 #       continue #continue 는 밑에것을 진행하지않고 다음 루프로 돌아감
 #   elif student in no_book:
 #       print("오늘 수업 여기까지야 {0}는 교무실로 따라와".format(student))
 #       break #break 은 다음 루프로 가는것이 아니라 아에 루프 밖으로 벗어남
 #   print("{0} 번아 책을 읽어봐".format(student))

#출석번호가 1,2,3,4 앞에 100을 붙이기로함 -> 101,102,103,104

student = [1,2,3,4,5]

print(student)
students = [i+100 for i in student]
print(students)

name= ["william", "sophie", "Daniel"]

name = [i.upper() for i in name]

print(name)