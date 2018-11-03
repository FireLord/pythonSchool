num=0
for row in range(1,6):
    for col in range(1,row):
        print(num,end="")
        if num==0:
            num+=1
    num*=2
    print()
