num=input("Enter your phone no(xxx-xxx-xxxx format):")
forValid=0 # this will increase if num has '-' at 3 place for 2times
numValid=0 # this will increase only if 10 digit num is given
for a in num:
    if a.isdigit():
        numValid+=1
    if (a==num[3] and a=="-") or (a==num[7] and a=="-"):
        forValid+=1
if forValid == 2: # set 2 bcz there can be only 2 '-' atq!
    print("phone num format VALID")
else:
    print("phone num format INVALID")
if numValid == 10: # set 10 bcz there can be only 10 digit num!
    print("phone num VALID")
else:
    print("phone num INVALID")
