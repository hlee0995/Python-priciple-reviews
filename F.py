def open_account():
    print("새로운 계좌가 생성되엇습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
     print("출금이 완료되었습니다 잔액은 {0}입니다".format(balance - money))
     return balance - money

    else: print("출금을 할 수 없습니다")
    return balance

    
balance = 0 

balance = deposit(balance, 5000)

print(balance)

balance = withdraw(balance, 500)

print (balance)


