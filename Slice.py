Jumin ="950917-1660543"

print("성별: " + Jumin[7])
print("년 : " + Jumin[0:2]) #2전까지
print("월 : " + Jumin[2:4]) 

print("생년월일 : " + str(Jumin[:6])) #처음부터 6직전까지
print("뒤 7자리 : " + str(Jumin[7:])) #7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + str(Jumin[-7:]))

python = "PYTHON IS AMAZINg"

print(python.lower()) #로워로 바꿔줘
print(python.upper()) #어퍼로 바꿔줘

print(python[0].isupper()) #python 의 첫글자가 upper 인가요? Bool 로 대답

print(len(python)) #길이 리턴
print(python.replace("PYTHON", "JAVA"))

index = python.index("N") 
print(index)

index = python.index("N", index + 1) #처음에 인덱스 찾았을떄 5번째 그다음부터 search 함 
print(index)

print(python.find("N")) # 내가 원하는 값이 없을땐 -1을 반환
print(python.find("JAVA")) #인덱스로 하게되면 오류가남
print(python.index("JAVA")) #subsrting not found

print(python.count("N")) #N의 갯수 카운트 



