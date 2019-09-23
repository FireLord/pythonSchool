x={"k1":"v1","k2":"v2","k3":"v3"}
inverted_x = dict([v,k] for k,v in x.items())
print(inverted_x)