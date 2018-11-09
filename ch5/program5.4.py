line=input("Enter a line:")
upperCount=lowerCount=digCount=alphaCount=0
for a in line:
    if a.isupper():
        upperCount+=1
    elif a.islower():
        lowerCount+=1
    elif a.isdigit():
        digCount+=1
    if a.isalpha():
        alphaCount+=1
print("Number of uppercase letter:",upperCount)
print("Number of lowercase letter:",lowerCount)
print("Number of alphabets letter:",alphaCount)
print("Number of digits:",digCount)