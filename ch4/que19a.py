#FIXME:
upper=2
lower=9
add=div=0
for i in range(1,4):
    if i==2:
        div=div-(upper/lower)
    else:
        div=add-(upper/lower)
    upper+=3
    lower+=4
    if i!=1:
        add=div+(upper/lower)
print(div)
