###############################
##         Pro way           ##
##############################
num = int(input("Enter the number of rows:"))
for i in range(num):
    print(" "*(num-i-1)+"* "*(i+1))
for j in range(num-1, 0, -1):
    print(" "*(num-j)+"* "*(j))

# Long way (above code in little more step
#           so that i can relate later on)
for v in range(0, num):
    for a in range(0, num-v-1):
        print(end=" ")
    for a in range(0, v+1):
        print("*", end=" ")
    print()
for n in range(num-1, 0, -1):
    for s in range(0, num-n):
        print(end=" ")
    for s in range(0, n):
        print("*", end=" ")
    print()

###############################
##         Semi-pro way      ##
##############################
for row in range(1, 6):
    for col in range(1, 6):
        if row+col == 4 or col-row == 2 or col-row == -2 or col+row == 8:
            print("*", end="")
        else:
            print(end=" ")
    print()
###############################
##         Noob way          ##
##############################
for row in range(1, 6):
    for col in range(1, 6):
        if (row == 3 and col == 1) or (row == 3 and col == 3) or (row == 3 and col == 5) or (row == 2 and col == 2) or (row == 2 and col == 4) or (row == 1 and col == 3) or (row == 4 and col == 2) or (row == 4 and col == 4) or (row == 5 and col == 3):
            print("*", end="")
        else:
            print(end=" ")
    print()
