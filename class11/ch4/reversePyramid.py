num=int(input("Enter number of rows:"))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

# Short way
for v in range(num,0,-1):
    print(" "*(num-v)+"* "*(v))
