a=input("Enter first value")
b=input("Enter second value")
c=input("Enter third value")
d=input("Enter fourth value")

if ((a>b) and (a>c) and (a>d)):
    print(a, "is greatest")
elif ((b>a) and (b>c) and (b>d)):
    print(b, "is greatest")
elif ((c>a) and (c>b) and (c>d)):
    print(c, "is greatest")
else:
    print(d, "is greatest")