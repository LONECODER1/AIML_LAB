def mm(n,d,a,b,m):
    if d==0 or n not in g:return v[n]
    if m:
        x=float("-inf")
        for c in g[n]:
            x=max(x,mm(c,d-1,a,b,0));a=max(a,x)
            if a>=b:break
        return x
    else:
        x=float("inf")
        for c in g[n]:
            x=min(x,mm(c,d-1,a,b,1));b=min(b,x)
            if a>=b:break
        return x
g={1:[2,3],2:[4,5],3:[6,7]};v={4:3,5:5,6:2,7:9}
print(mm(1,3,-9e9,9e9,1))
