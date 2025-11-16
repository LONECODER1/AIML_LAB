g={"A":[("B","C")],"B":[("D","E")],"C":[("G",)]}
def ao(n):
    if n not in g:return[n]
    for x in g[n]:
        r=[] 
        for y in x:r+=ao(y)
        return[n]+r
print(ao("A"))
