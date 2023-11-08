def print_board(board):
    print("-------------", end="\n| ")
    for i in range(3):
        for j in range(3):
            if board[i][j] == 2:
                print(" ", end=" | ")
            elif board[i][j] == 3:
                print("X", end=" | ")
            elif board[i][j] == 5:
                print("O", end=" | ")
        print("\n-------------", end="\n| ")
    print()

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(all(cell != 2 for cell in row) for row in board)

def tic_tac_toe():
    board = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    player = 3  # 'X' starts
    moves = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            if moves % 2 == 0:
                move = int(input(f"Player 'X', enter your move (1-9): "))
            else:
                move = int(input(f"Player 'O', enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] != 2:
                print("That position is already occupied. Try again.")
                continue

            board[row][col] = player
            moves += 1
            print_board(board)

            if check_win(board, player):
                print(f"Player '{'X' if player == 3 else 'O'}' wins!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            player = 3 if player == 5 else 5

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    tic_tac_toe()