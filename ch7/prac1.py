lst1 = list(input("Enter list of numbers:"))
num = input("Enter the number you want to find:")
length = len(lst1)
indexValue = ""
for a in range(length):
    if lst1[a] == num:
        indexValue += str(a)+" "  # Here i add all index num with space in end.
print("The number", num, "in list", lst1, "has indexes", indexValue)
