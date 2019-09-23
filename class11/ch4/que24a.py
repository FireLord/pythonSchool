char=input("Enter start alpha:")
num=int(input("Enter num of rows:"))
charNum=int(ord(char))
charInt=charNum-1
for row in range(1,num+1):
    for col in range(1,row):
        print(chr(charInt),end="")
    charInt+=1
    print()