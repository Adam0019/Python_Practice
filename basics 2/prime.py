a=int(input("enter a number: "))

def prime(a):
    c=0
    for i in range (2, a):
        if a%i == 0:
            c=c+1
            break
    if c == 0:
        return 0
    else:
        return 1

result = prime(a)

if result == 0:
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")