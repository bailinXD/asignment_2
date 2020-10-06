from os import system, name

def main():
    while True:
        try:
            rows = int(input('rows = '))
            columns = int(input('columns = '))
            if rows > 0 and columns > 0:
                break
            else:
                print('Not valid input...Try again')
        except ValueError:
            print('Not valid input...Try again')

    grid = [[] for gridlist in range(rows)]
    print('grid =')
    for rowloop in range(rows):
        temline = input()
        while len(temline) != columns or temline.count('1') + temline.count('0') != columns:
            temline = input('Not valid input...Try again')
        grid[rowloop] = list()
    num = 0
    for rowloop in range(rows):
        for columnloop in range(columns):
            if grid[rowloop][columnloop] == '1':
                grid, area = infect_grid(grid, rows, columns, rowloop, columnloop, 0)
                if area > 1:
                    num += 1
    print('Number of stores: ', num)



def infect_grid(grid, rows, columns, row, column, area):
    if grid[row][column] == '1':
        grid[row][column] = '2'
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


main()
