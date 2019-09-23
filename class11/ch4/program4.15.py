n = int(input("Enter the natural num limit:"))
sumOdd = sumEven = 0
ctr = 1
while ctr <= n:
    if ctr % 2 == 0:
        sumEven += ctr
    else:
        sumOdd += ctr
    ctr += 1
print("The sum of even int is:", sumEven)
print("The sum of odd int is:", sumOdd)
