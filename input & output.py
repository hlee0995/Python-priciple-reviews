#print("Python", "Java", sep=",", end="?") #sep는 사이에 무엇이 들어갈지 설정해줌 #end 는 끝나는 부분을 설정

scores = {"수학": 0, "영어": 90, "국어":40}

for subject, scores in scores.items():
    print(subject.ljust(8), str(scores).rjust(4),sep="") #왼쪽정렬 우측정렬


#은행 대기 순번표

for Num in range(1,21):
    print("대기번호: " + str(Num).zfill(3))