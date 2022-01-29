###Quiz 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오 
#1: HTTP:// 부분은 제외 
#2: 처음 만나는 점 이후 부분은 제외
#3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 

#EX) naver.com    nav51!

site = input("사이트를 입력하세요: ")
#http://naver.com

site = site.replace("http://", "")
site = site[:site.index(".")]
ID = site[0:3] + str(len(site)) + str(site.count('e')) + "!"
print(ID)


