from collections import deque
s=("door","floor","away")
g=("door","top","with")
q=deque([s]);v={s};p={s:[]}
moves=[("move","banana","chair"),("push","floor","chair"),("climb","chair","top"),("grab","top","with")]
while q:
    x=q.popleft()
    if x==g:print(p[x]);break
    for m in moves:
        y=(x[0],m[2],x[2]) if m[0]=="climb" else x
        if y not in v:v.add(y);p[y]=p[x]+[m];q.append(y)
