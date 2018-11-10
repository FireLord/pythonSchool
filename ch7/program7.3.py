lst=eval(input("Enter list:"))
length=len(lst)
minEle=lst[0]
minIndex=0
for i in range(1,length-1):
    if lst[i] < minEle:
        minEle=lst[i]
        minIndex=i
print("Give list is:",lst)
print("The min element of the given list is:")
print(minEle,"at index",minIndex)