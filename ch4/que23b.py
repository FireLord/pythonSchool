num=int(input("Enter num of rows:"))
for i in range(0,num):
    for j in range(0,i):
        print("*",end=" ")
    print()
for k in range(num,0,-1):
    for p in range(0,k):
        print("*",end=" ")
    print()

# short way
for q in range(0,num):
    print("* "*(q))
for z in range(num,0,-1):
    print("* "*(z))