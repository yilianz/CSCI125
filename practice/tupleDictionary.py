import math

def findRV(a,b,c):
    root1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    root2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    Vx = (-b)/(2*a)
    Vy = a*Vx**2+b*Vx+c
    return (root1,root2,Vx,Vy)


a = input("please enter the coeficient of quadratic function a x^2+ bx+ c  \na= ")
b = input("b= ")
c = input("c=")

ans = findRV(float(a),float(b),float(c))

print(f'For function {a}x^2+{b}x+{c}\nThe vetex is {(ans[2],ans[3])} \nThe root are {(ans[0],ans[1])} ')
