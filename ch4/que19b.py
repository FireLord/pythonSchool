n=int(input("Enter a value:"))
sum=0
while n>0:
    if n%2!=0:
        sum+=n**2
    n-=1
print(sum)