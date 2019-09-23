upper=int(input("Enter the upper limit for the range:"))
sum=0
print("Odd numbers are :")
for i in range(1, upper+1):
    if(i % 2 != 0):
        sum+=i
        print(i)
print('Sum of odd numbers =', sum)
