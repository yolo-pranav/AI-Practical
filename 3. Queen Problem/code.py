def is_safe(board, row, col):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_8_queens(board, col, solutions):
    if col >= len(board):
        solutions.append([row[:] for row in board])
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_8_queens(board, col + 1, solutions)
            board[i][col] = 0

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            row_str = ''.join('Q ' if cell == 1 else '_ ' for cell in row)
            print(row_str)
        print()

def find_all_fundamental_solutions():
    board_size = 8
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    solutions = []
    solve_8_queens(board, 0, solutions)
    return solutions

def is_fundamental_solution(solution, fundamental_solutions):
    # Rotate and mirror the solution and compare to existing fundamental solutions
    rotated_solutions = []
    for _ in range(4):
        rotated_solutions.append([''.join('Q ' if cell == 1 else '_ ' for cell in row) for row in solution])
        solution = list(zip(*reversed(solution)))

    for rotated in rotated_solutions:
        if rotated in fundamental_solutions:
            return False
    return True

fundamental_solutions = []
solutions = find_all_fundamental_solutions()
for solution in solutions:
    if is_fundamental_solution(solution, fundamental_solutions):
        fundamental_solutions.append(solution)

print_solutions(fundamental_solutions[:12])