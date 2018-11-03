# hardCoded row
for row in range(1, 6):
    for col in range(1, 6):
        if row+col == 4 or row+col == 8 or col-row == 2 or col-row == -2:
            print("*", end="")
        else:
            print(end=" ")
    print()

# userDep row.
# BUG: row will be generated (n*2)-1 times
n = int(input("Enter num of rows:"))
for row in range(1, n+1):
    for col in range(1, 2*n):
        if row+col == n+1 or col-row == n-1:
            print("*", end="")
        else:
            print(end=" ")
    print()
for row in range(2, n+1):
    for col in range(1, 2*n):
        if row+col == 2*n or col-row == 0:
            print("*", end="")
        else:
            print(end=" ")
    print()
