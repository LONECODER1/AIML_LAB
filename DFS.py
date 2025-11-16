g = {1:[2,3], 2:[4], 3:[4], 4:[]}
vis = set()

def dfs(u):
    print(u, end=" ")
    vis.add(u)
    for v in g[u]:
        if v not in vis:
            dfs(v)

dfs(1)
