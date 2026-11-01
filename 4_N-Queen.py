
def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):

    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    # All queens are placed
    if row == n:
        return True

    # Try each column in the current row
    for col in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 1

            # Recursively place next queen
            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False



# Main program
n = int(input("Enter the value of N: "))

board = [[0 for j in range(n)] for i in range(n)]

if solve_n_queens(board, 0, n):
    print("Solution for", n, "Queens:")
    print_solution(board, n)
else:
    print("No solution exists")
    
    
    
# Enter the value of N: 4
# Solution for 4 Queens:
# 0 1 0 0 
# 0 0 0 1 
# 1 0 0 0 
# 0 0 1 0 

# Enter the value of N: 2
# No solution exists


# Time Complexity: O(N!)
# Space Complexity: O(N²)