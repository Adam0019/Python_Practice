a=int(input("Enter the number: "))
s=0
y=a
while(a>0):
    p=a%10
    s=s*10+p
    a=a//10
if (y==s):
    print(y,"The number is  a palindrome.")
else:
    print(y,"The number is not a palindrome")