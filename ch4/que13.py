N=int(input("Enter a num:"))
while N:
    if N%3==0 and N%7==0:
        print("TipsyTopsy")
    elif N%3==0:
        print("Tipsy")
    elif N%7==0:
        print("Topsy")
    else:
        print(N)
    N-=1
