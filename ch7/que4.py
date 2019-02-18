lst1=eval(input("Enter a list of strings:"))
lst2=[]
for a in lst1:
    length=len(a)
    word=a[1:length]
    lst2+=[word]
print(lst2)