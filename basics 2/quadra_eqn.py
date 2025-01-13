import cmath    #calling the library
a=int(input("Enter the fist digit: "))       #taking user input
b=int(input("Enter the second digit: "))
c=int(input("Enter the third digit: "))

def quad(a,b,c):                         #defining the function
     dis=cmath.sqrt(b**2 - 4*a*c)
     print(dis)
     root1= (- b + dis)/(2*a)
     root2= (- b - dis)/(2*a)
     print("The first root is: ", root1)
     print("The second root is: ", root2)
quad(a,b,c)