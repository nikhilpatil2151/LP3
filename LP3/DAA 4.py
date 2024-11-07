N = 8  # Size of the board

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    # If all queens are placed
    if col >= N:
        return True

    # Try placing a queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solve_nq_util(board, col + 1):
                return True

            # If placing  queen doesn't lead to a solution, BACKTRACK
            board[i][col] = 0

    return False

def solve_nq(first_row, first_col):
    board = [[0 for _ in range(N)] for _ in range(N)]  # Initialize board

    # Place the first queen
    board[first_row][first_col] = 1

    # Solve for the next column
    if not solve_nq_util(board, 1):  # Start from column 1
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

# Driver program to test above functions
if __name__ == "__main__":
    first_row = 0  # Change to your desired row (0-7)
    first_col = 0  # Change to your desired column (0-7)
    
    # Ensure the first queen is placed within the bounds
    if first_row >= N or first_col >= N:
        print("Invalid position for the first queen.")
    else:
        solve_nq(first_row, first_col)
