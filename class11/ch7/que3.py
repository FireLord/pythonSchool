lst=eval(input("Enter a list(num between 1-12):"))
lim=len(lst)
for a in range(0,lim):
    if lst[a]>10:
        lst.pop(a)
        lst.insert(a,'10')
print(lst)