s=input("Expression: ")
f=s.split()
x,y,z=f
x=int(x)
z=int(z)
if y=='+':
    d=x+z
    d=float(d)
    print(d)
elif y=='-':
    d=x-z
    d=float(d)
    print(d)
elif y=='*':
    d=x*z
    d=float(d)
    print(d)
elif y=='/':
    d=x/z
    d=float(d)
    print(d)
