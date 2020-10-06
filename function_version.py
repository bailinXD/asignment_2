from os import system, name

def stores_analysis(rows, columns, grid):
    num = 0
    for rowloop in range(rows):
        for columnloop in range(columns):
            print(grid[rowloop][columnloop])
            if grid[rowloop][columnloop] == 1:
                grid, area = infect_grid(grid, rows, columns, rowloop, columnloop, 0)
                if area > 1:
                    num += 1
    return num

def infect_grid(grid, rows, columns, row, column, area):
    if grid[row][column] == 1:
        grid[row][column] = 2
        area += 1
        if row - 1 >= 0:
            grid, area = infect_grid(grid, rows, columns, row - 1, column, area)
        if row + 1 < rows:
            grid, area = infect_grid(grid, rows, columns, row + 1, column, area)
        if column - 1 >= 0:
            grid, area = infect_grid(grid, rows, columns, row, column - 1, area)
        if column + 1 < columns:
            grid, area = infect_grid(grid, rows, columns, row, column + 1, area)
    return grid, area

stores_analysis(5, 4, [[1,1,0,0],[0,0,1,0],[0,0,0,0],[1,0,1,1],[1,1,1,1]])
