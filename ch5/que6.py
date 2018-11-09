##########
# FIXME: #
##########
# TODO: Need to work more on logic. not getting
# correct pattern.
string1 = input("Enter first string:")
string2 = input("Enter second string:")
sum1 = sum2 = 0
for a in string1:
    sum1 += ord('a')
for b in string2:
    sum2 += ord('b')
if sum1 > sum2:
    print(string2)
    x = 0
    lim = len(string1)
    for row in range(1, lim-2):
        for col in range(1, lim+1):
            if row+col == lim+1 or row-col == 0:
                print(string1[x], end="")
                x += 1
            else:
                print(end=" ")
        print()
else:
    print(string1)
    x = 0
    lim = len(string2)
    for row in range(1, lim-2):
        for col in range(1, lim+1):
            if row+col == lim+1 or row-col == 0:
                print(string2[x], end="")
                x += 1
            else:
                print(end=" ")
        print()