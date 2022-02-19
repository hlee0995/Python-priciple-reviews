student_height = input("Input a list of student heights: ").split()
print(student_height)
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
# text into int type
print(student_height)
total = 0

#for n in range(0, len(student_height)):
#    total += student_height[n]
for i in student_height:
    total += i
average = total / (n+1) 
average = round(average)
print(average)




