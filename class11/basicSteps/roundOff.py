x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
if(x<y):
    diff=y-x
    if (diff<=0.001):
        print(diff,"Close")
    else:
        print(diff,"Not close")
else:
    diff=x-y
    if (diff<=0.001):
        print(diff,"Close")
    else:
        print(diff,"Not close")