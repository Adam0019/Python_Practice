l=[]
a= int(input("Enter a num"))
f=1
for i in range ( 1, a+1):
    f=f*i
    print(f)

l.append(f)

print(l)

b=int(input("Enter a num"))
o=1
for i in range ( 1, b+1):
    o=o*i
    print(o)

d=f+o
l.append(d)
print(l)

l.reverse()
print(l)