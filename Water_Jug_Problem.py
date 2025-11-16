from collections import deque
def solve(a,b,t):
    q=deque([(0,0)]);v=set()
    while q:
        x,y=q.popleft()
        if x==t or y==t:return(x,y)
        if (x,y) in v:continue
        v.add((x,y))
        q+= [(a,y),(x,b),(0,y),(x,0),(min(a,x+y),max(0,x+y-a)),(max(0,x+y-b),min(b,x+y))]
print(solve(4,3,2))
