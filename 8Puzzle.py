from collections import deque
def solve(s,g):
    q=deque([s]);v={s};p={s:""}
    while q:
        x=q.popleft()
        if x==g:return p[x]
        i=x.index("0")
        for d in [1,-1,3,-3]:
            j=i+d
            if 0<=j<9 and not(i%3==2 and j%3==0) and not(i%3==0 and j%3==2):
                y=list(x);y[i],y[j]=y[j],y[i];y="".join(y)
                if y not in v:v.add(y);p[y]=p[x]+y+" ";q.append(y)
print(solve("123405678","123456780"))
