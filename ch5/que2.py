string=input("Enter a string:")
sumInt=0
sumAlpha = ""  # empty string for concatenation
for a in string:
    if a.isdigit():
        sumAlpha += a  # here I concatenated the available digits for ques.
        sumInt+=int(a) # here I converted the digit string to int and added
if sumAlpha=="":
    print(string,"has no digits")
else:
    print(string,"has digits",sumAlpha,"which has sum to",sumInt)
