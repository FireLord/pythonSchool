a=input("Enter first value")
b=input("Enter second value")
c=input("Enter third value")

if ((a>b) and (a>c)):
    print(a, "is greatest")
elif ((b>a) and (b>c)):
    print(b, "is greatest")
else:
    print(c, "is greatest")