for waiting_no in range(5): #0에서 5 미만까지
    print("대기번호: {0}".format(waiting_no))

for waiting_no in range(1,6): #1에서 6 미만까지
    print("대기번호: {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되엇습니다.".format(customer))

for customer in starbucks:
    print("{0}, 커피가 준비되엇습니다.".format(starbucks)) #요렇게하면 스타벅스 안에있는걸 돌리는게 아니라 전부다가 3번씩 됨