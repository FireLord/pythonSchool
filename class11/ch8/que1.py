first = 0
second = 1
l1=[first,second]
for a in range(1,8):
    third=first+second
    l1+=[third]
    first,second=second,third
t1=tuple(l1)
print(t1)