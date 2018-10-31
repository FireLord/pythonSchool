item=int(input("Enter no of items:"))
if (item>=100):
    cost=item*70
    print("You have bought,",item,"items and your total amount in INR is",cost)
elif (10<=item<=100):
    cost=item*100
    print("You have bought,",item,"items and your total amount in INR is",cost)
elif (0<=item<=10):
    cost=item*120
    print("You have bought,",item,"items and your total amount in INR is",cost)
else:
    print("Invalid input")