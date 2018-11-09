i = 1
s2 = ""
while i > 0:
    s = input("Enter a sentence(press q to quit):")
    if s == "q":
        break
    for a in s:
        if a.isupper():  # if char is upper make it lower
            s2 += a.lower()
        elif a.islower():  # if char is lower make it upper
            s2 += a.upper()
        else:  # if char is not lower/upper mostly num or special char then just add it
            s2 += a
    print(s2)
    s2 = "" # set string2 as empty again so that new sentence is fresh
