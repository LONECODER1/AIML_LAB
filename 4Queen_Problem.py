# 4-Queens Problem (Simple & Compact)

N = 4
sol = []

def safe(board, r, c):
    for i in range(r):
        if board[i] == c or abs(board[i] - c) == abs(i - r):
            return False
    return True

def solve(r, board):
    if r == N:
        sol.append(board[:])
        return
    for c in range(N):
        if safe(board, r, c):
            board[r] = c
            solve(r + 1, board)

solve(0, [-1]*N)

for s in sol:
    for r in s:
        print("."*r + "Q" + "."*(N-r-1))
    print()
