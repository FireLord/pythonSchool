num=int(input("Enter the number of rows:"))
for i in range(num):
    print(" "*(num-i-1)+"* "*(i+1))
for j in range(num-1,0,-1):
    print(" "*(num-j)+"* "*(j))

# Long way
for v in range(0,num):
    for a in range(0,num-v-1):
        print(end=" ")
    for a in range(0,v+1):
        print("*",end=" ")
    print()
for n in range(num-1,0,-1):
    for s in range(0,num-n):
        print(end=" ")
    for s in range(0,n):
        print("*",end=" ")
    print()