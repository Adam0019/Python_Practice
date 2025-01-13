n=int(input("Enter a number: "))
s=0
t=n
while t>0:
    d=t%10
    s+=d**3
    t//=10
if n==s:
    print(n,"is Armstrong")
else:
    print(n,"is not Armstrong")