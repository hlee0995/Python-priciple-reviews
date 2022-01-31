#표준 채중을 구하는 프로그램을 작성하시오

#표준 체중: 각 개인의 키에 적당한 체증

#성별에 따른 공식

#남자: 키(m) * 키(m) *22
#여자: 키(m) * 키(m) *21

#조건1: 표준 체중은 별도의 함수 내에서 계산
#        * 함수명 : std_weight
#        * 전달값 : 키(height), 성별(gender)

#조건2: 표준 체중은 소수점 둘째자리까지 표시

#출력예제
#EX) 키 175cm 남자의 표준 체중은 67.38kg 입니다

#input 으로 키 받기



#표준체중 구하기




def std_weight(height, gender):
    if gender == "M":
        return height * height * 22
    else:
        return height * height *21

height = 175
gender = "M"

weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}KG 입니다".format(height, gender, weight))




#프린트하기

