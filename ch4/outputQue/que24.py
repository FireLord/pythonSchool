import math

# Gcd function
x=int(input("Enter number for x :"))
y=int(input("Enter number for y :"))
gcd=math.gcd(x,y)

# Lcm function
lcm = (x*y)//gcd

print("Gcd of x and y :",gcd)
print("Lcm of x and y :",lcm)
