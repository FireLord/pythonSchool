d1={}
i=1
while i>0:
    teamName=input("Enter name of team:")
    win=int(input("Enter times won:"))
    loss=int(input("Enter times lost:"))
    d1[teamName]=[win,loss]
    q=input("Press q to quit:")
    if q=="q":
        break
# a part
teamNameList=input("Enter team:")
val=d1[teamNameList]
total=val[0]+val[1]
winPer=(val[0]/total)*100
print(teamNameList,"winning percentage is",winPer)
