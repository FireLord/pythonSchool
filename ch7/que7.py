lst1=eval(input("Enter a list:"))
lim=len(lst1)
for a in range(lim):
    lst1[a+1]=lst1[a]
lst1.pop(0)
print(lst1)
