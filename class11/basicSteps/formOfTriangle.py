a=float(input("Enter first side of triangle :"))
b=float(input("Enter second side of triangle :"))
c=float(input("Enter third side of triangle :"))
if ((a<0) or (b<0) or (c<0)):
    print("Invalid input")
else:
    if ((a+b>c) or (b+c>a) or (c+a>b)):
        print("Triangle will form")
    else:
        print("Triangle will not form")