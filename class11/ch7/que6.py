l=list(input("Enter num for list 1:"))
m=list(input("Enter num for list 2:"))
n=[]
lim=len(l)
for a in range(lim):
    sum=int(l[a])+int(m[a])
    n+=[sum]
print(n)