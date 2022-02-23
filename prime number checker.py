n = int(input("Check this number: "))
i= 2

def prime_checker(number=n):
    while i < n : 
        if n % i == 0:
            print(f"The number {n} is not a prime number")
            break;
        else:
            print(f"The number {n} is a prime number")
            break;


prime_checker(n)
