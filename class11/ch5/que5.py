string1 = int(input("Enter a num:"))
string2 = input("Enter a string:")
alphaCount = ""
for a in string2:
    if a.isdigit():
        alphaCount += a
if alphaCount == "":  # if the string has no digit then set alphaCount to 0
    alphaCount = 0    # this is to avoid error while using the var in sum func.
sum = string1+int(alphaCount)  # here I converted the concatenated alphaCount to int, to add
print("Int value:", string1)
print("string value:", string2)
print("int+extractedInt:", string1, "+", alphaCount, "=", sum)