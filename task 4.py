def print_board(board):
    """Print the Sudoku board in a visually appealing way."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Print horizontal separator every 3 rows
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  # Print vertical separator every 3 columns
            if j == 8:
                print(board[i][j])  # Print new line at the end of each row
            else:
                print(f"{board[i][j]} ", end="")


def find_empty(board):
    """Find an empty cell in the board. Returns (row, col) tuple or None."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, pos):
    """Check if placing num at position pos is valid."""
    row, col = pos

    # Check row
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Reset if no valid number found

    return False


def main():
    # Example Sudoku puzzle (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # another option
    # board = [
    #     [0, 0, 0, 2, 6, 0, 7, 0, 1],
    #     [6, 8, 0, 0, 7, 0, 0, 9, 0],
    #     [1, 9, 0, 0, 0, 4, 5, 0, 0],
    #     [8, 2, 0, 1, 0, 0, 0, 4, 0],
    #     [0, 0, 4, 6, 0, 2, 9, 0, 0],
    #     [0, 5, 0, 0, 0, 3, 0, 2, 8],
    #     [0, 0, 9, 3, 0, 0, 0, 7, 4],
    #     [0, 4, 0, 0, 5, 0, 0, 3, 6],
    #     [7, 0, 3, 0, 1, 8, 0, 0, 0]
    # ]

    print("\nOriginal Sudoku Board:")
    print_board(board)

    if solve(board):
        print("\nSolved Sudoku Board:")
        print_board(board)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")


if __name__ == "__main__":
    main()
