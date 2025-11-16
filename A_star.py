from heapq import heappush,heappop
def astar(s,g,h,f):
    q=[];heappush(q,(h(s),s,[]));v=set()
    while q:
        _,n,p=heappop(q)
        if n==g:return p+[n]
        if n in v:continue
        v.add(n)
        for x in f[n]:heappush(q,(h(x),x,p+[n]))
