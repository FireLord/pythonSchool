d1={}
i=1
while i>0:
    name=input("Enter the name of the product:")
    price=int(input("Enter the price of the product:"))
    d1[name]=price
    q=input("Press q when done with listing product:")
    if q=="q":
        productName=input("Enter product name to check:")
        t1=d1.items()
        l1=[]
        for a in t1:
            l1+=a
        for b in l1:
            if productName==a:
                print("Price of",productName,"is",d1[productName])
            else:
                print("Product not in dict.")
        break