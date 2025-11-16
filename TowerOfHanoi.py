def h(n,a,b,c):
    if n: h(n-1,a,c,b);print(a,"->",c);h(n-1,b,a,c)
h(3,"A","B","C")
