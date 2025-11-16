from itertools import permutations
d=[[0,3,4,2],[3,0,1,5],[4,1,0,6],[2,5,6,0]]
n=len(d)
best=1e9;p=[]
for x in permutations(range(n)):
    c=sum(d[x[i]][x[(i+1)%n]] for i in range(n))
    if c<best:best=c;p=x
print(best,p)
