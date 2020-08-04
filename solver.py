import numpy as np

grid = [
[4, 0, 0, 0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 9, 8],
[3, 0, 0, 0, 8, 2, 4, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 8, 0],
[9, 0, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 0, 6, 7, 0],
[0, 5, 0, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 2, 0, 0, 9, 0, 7],
[6, 4, 0, 3, 0, 0, 0, 0, 0],
]
print(np.matrix(grid))
def possible(grid,row,col,n):
    for i in range(9):
        if grid[row][i] == n:
            return False
    for i in range(9):
        if grid[i][col] == n:
            return False
    x0 = (row//3) * 3
    y0 = (col//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j] == n:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1,10):
                    if possible(grid,row,col,n):
                        grid[row][col] = n
                        solve(grid)
                        grid[row][col] = 0
                return
    print(np.matrix(grid))
    print_sudoku(grid)
    input("More?")

def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")


print_sudoku(grid)
solve(grid)
