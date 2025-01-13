n=int(input("Enter the range: "))
def fibo(n):
    a=0
    b=1
    print(a)
    i=1
    while(i<(n-2)):
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
fibo(n)