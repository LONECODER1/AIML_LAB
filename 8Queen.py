N=8;a=[]
def safe(b,r,c):
    for i in range(r):
        if b[i]==c or abs(b[i]-c)==abs(i-r):return 0
    return 1
def solve(r,b):
    if r==N:a.append(b[:]);return
    for c in range(N):
        if safe(b,r,c):b[r]=c;solve(r+1,b)
solve(0,[-1]*8)
print(a)
