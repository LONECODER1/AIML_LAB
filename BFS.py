from collections import deque

g = {1:[2,3], 2:[4], 3:[4], 4:[]}
vis = set()
q = deque([1])

while q:
    u = q.popleft()
    if u in vis: continue
    vis.add(u)
    print(u, end=" ")
    for v in g[u]:
        q.append(v)
