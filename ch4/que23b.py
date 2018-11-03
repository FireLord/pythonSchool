###############################
##         Pro way           ##
##############################
num = int(input("Enter num of rows:"))
for q in range(0, num):
    print("* "*(q))
for z in range(num, 0, -1):
    print("* "*(z))

# Long way (above code in little more step
#           so that i can relate later on)
for i in range(0, num):
    for j in range(0, i):
        print("*", end=" ")
    print()
for k in range(num, 0, -1):
    for p in range(0, k):
        print("*", end=" ")
    print()

###############################
##         Semi-pro way      ##
##############################
for row in range(1, 6):
    for col in range(1, 4):
        if row == 3 or col == 1 or col == row or row+col == 6:
            print("* ", end="")
        else:
            print(end=" ")
    print()