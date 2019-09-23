d1={"jan":31,"feb":28,"mar":31,"apr":30,
    "may":31,"jun":30,"july":31,"aug":31,
    "sept":30,"oct":31,"nov":30,"dec":31}
# a part
monNam=input("Enter the name of month:")
print("No of days in",monNam,":",d1[monNam])
# b part
print("Months in ASC order:",d1.keys())
# c part
t1=d1.items()
l1=[]
for a in t1:
    l1+=a
for b in range(len(l1)):
    if l1[b]==31:
        print("Months with 31 days:",l1[b-1])