n = int(input("Enter num limit:"))
sum = 0
i = 1
while i <= n:
    if i % 2 != 0:
        sum += i
    i += 1
print("Sum of odd no is", sum)