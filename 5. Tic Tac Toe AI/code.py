board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    print('-' * 13)
    for row in board:
        print('| '+' | '.join(row)+' |')
        print('-' * 13)

def is_game_over(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    if ' ' not in [cell for row in board for cell in row]:
        return True

    return False

def evaluate(board):
    for row in board:
        if row.count('X') == 3:
            return 10
        if row.count('O') == 3:
            return -10

    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count('X') == 3:
            return 10
        if check.count('O') == 3:
            return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if not any(' ' in row for row in board):
        return 0

    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '

        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

while True:
    print_board(board)
    if not any(' ' in row for row in board) or is_game_over(board):
        break

    player_row, player_col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
    if board[player_row - 1][player_col - 1] == ' ':
        board[player_row - 1][player_col - 1] = 'O'
    else:
        print("Invalid move. Try again.")
        continue

    if is_game_over(board):
        print_board(board)
        print("You win!")
        break

    computer_row, computer_col = find_best_move(board)
    board[computer_row][computer_col] = 'X'

    if is_game_over(board):
        print_board(board)
        print("Computer wins!")
        break

    if not any(' ' in row for row in board):
        print_board(board)
        print("It's a draw!")
        break