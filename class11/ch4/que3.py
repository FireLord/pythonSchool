x=float(input("Enter first number :"))
y=float(input("Enter second number :"))
if (x>y):
    diff=x-y
    if (diff<=0.001):
        print(diff,"Number is close")
    else:
        print(diff,"Number is not close")
else:
    diff=y-x
    if (diff<=0.001):
        print(diff,"Number is close")
    else:
        print(diff,"Number is not close")
