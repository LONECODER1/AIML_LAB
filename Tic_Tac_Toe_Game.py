# Simple Tic-Tac-Toe

board = [" "] * 9
player = "X"

def show():
    print("\n".join([" | ".join(board[i:i+3]) for i in range(0, 9, 3)]), "\n")

def win():
    lines = [(0,1,2),(3,4,5),(6,7,8),
             (0,3,6),(1,4,7),(2,5,8),
             (0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] != " " for a,b,c in lines)

for _ in range(9):
    show()
    move = int(input(f"Player {player}, choose 0-8: "))

    if board[move] != " ":
        print("Spot taken! Try again.")
        continue

    board[move] = player

    if win():
        show()
        print(player, "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    show()
    print("It's a draw!")
