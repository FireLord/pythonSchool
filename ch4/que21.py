n=1
ageI = ageII = ageIII = 0
while n>0:
    age=int(input("Enter age of emp(press 0 to quit):"))
    if age==0:
        n-=1
    if 26<=age<=35:
        ageI+=1
    elif 36<=age<=45:
        ageII+=1
    elif 46<=age<=55:
        ageIII+=1
    elif 1<=age<=25 or age>=56:
        print("Age out of range")
    else:
        print("Wrong input!!!")
print("People in age 26 to 35 are:",ageI)
print("People in age 36 to 45 are:",ageII)
print("People in age 46 to 55 are:",ageIII)