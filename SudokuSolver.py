import math
import re

print("Welcome to the game of sudoku!\n")
sudoku = [
    [1, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 6, 0, 2, 0, 7, 0, 0],
    [7, 8, 9, 4, 5, 0, 1, 0, 3],
    [0, 0, 0, 8, 0, 7, 0, 0, 4],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 4, 2, 0, 1],
    [3, 1, 2, 9, 7, 0, 0, 4, 0],
    [0, 4, 0, 0, 1, 2, 0, 7, 8],
    [9, 0, 8, 0, 0, 0, 0, 0, 0]
]

while True:

    # default values used
    lst = []
    options = ['options']
    block_nums = []
    strikes = []

    for i in sudoku:
        print(i)

    # checks if the given input is the only available option for the block
    # if there are 2 or more available squares the player is guessing
    def check_options():
# ----------------------------------------------------------------------------------------
        if user_row in range(3) and user_column in range(3):
            k = 0, 3
            l = 0, 3
        elif user_row in range(3) and user_column in range(3, 6):
            k = 0, 3
            l = 3, 6
        elif user_row in range(3) and user_column in range(6, 9):
            k = 0, 3
            l = 6, 9
        elif user_row in range(3, 6) and user_column in range(3):
            k = 3, 6
            l = 0, 3
        elif user_row in range(3, 6) and user_column in range(3, 6):
            k = 3, 6
            l = 3, 6
        elif user_row in range(3, 6) and user_column in range(6, 9):
            k = 3, 6
            l = 6, 9
        elif user_row in range(6, 9) and user_column in range(3):
            k = 6, 9
            l = 0, 3
        elif user_row in range(6, 9) and user_column in range(3, 6):
            k = 6, 9
            l = 3, 6
        elif user_row in range(6, 9) and user_column in range(6, 9):
            k = 6, 9
            l = 6, 9

        for i in range(k[0], k[1]):
            for j in range(l[0], l[1]):
                lst.clear()
                if i == user_row and j == user_column:
                    pass
                elif sudoku[i][j] == 0:
                    run_script(i, j)
                    if len(lst) == 4:
                        options.clear()
# ----------------------------------------------------------------------------------------

    # Checks if the given input number isn't in the given input row
    def check_row(row):
        if user_number not in sudoku[row]:
            lst.append('row')

    # Checks if the given input number isn't in the given input column
    def check_column(column):
        sudoku_column = []
        for i in range(9):
            sudoku_column.append(sudoku[i][column])
        if user_number not in sudoku_column:
            lst.append('column')

    # Finds the block (1-9) the input number is in
    def find_block(row, column):
        new_row = math.ceil((row+1) / 3)
        new_column = math.ceil((column+1) / 3)
        if new_row == 1:
            block = new_column
            return block
        elif new_row == 2:
            block = new_row * 2 + new_column - 1
            return block
        elif new_row == 3:
            block = new_row * 2 + new_column
            return block

    # Checks if the input number isn't in block already (using the find_block() output)
    def check_block(block):
        sudoku_blocks = [
            [sudoku[i][j] for i in range(3) for j in range(3)],
            [sudoku[i][j] for i in range(3) for j in range(3,6)],
            [sudoku[i][j] for i in range(3) for j in range(6,9)],
            [sudoku[i][j] for i in range(3,6) for j in range(3)],
            [sudoku[i][j] for i in range(3,6) for j in range(3,6)],
            [sudoku[i][j] for i in range(3,6) for j in range(6,9)],
            [sudoku[i][j] for i in range(6,9) for j in range(3)],
            [sudoku[i][j] for i in range(6,9) for j in range(3,6)],
            [sudoku[i][j] for i in range(6,9) for j in range(6,9)],
        ]

        if user_number not in sudoku_blocks[block-1]:
            block_nums.append(block-1)
            lst.append('block')
            return True

    # Checks if the number square is available or not (0 means available)
    def check_available(user_row, user_column):
        if sudoku[user_row][user_column] == 0:
            lst.append('available')

    # finishes sudoku by looping every possible number at every possible spot
    def finish_sudoku():
        for i in range(9):
            for j in range(9):
                user_row = i
                user_column = j
                check_options()
                run_script(user_row, user_column)

    # asks for input using regex
    while True:
        user_choice = input("\nfinish/exit/Insert choice as row,column,number: ")
        pattern = "^(?=.{5}$)\d[,]\d[,]\d*$"
        result = re.findall(pattern, user_choice)
        if result or user_choice == 'finish' or 'exit':
            break
        else:
            print('Incorrect input!')

    if result:
        user_row = int(user_choice.split(',')[0])-1
        user_column = int(user_choice.split(',')[1])-1
        user_number = int(user_choice.split(',')[2])

    def run_script(user_row, user_column):
        check_row(user_row)
        check_column(user_column)
        check_block(find_block(user_row, user_column))
        check_available(user_row, user_column)

    # finishes sudoku by looping every possible number at every possible spot
    if user_choice == 'finish':
        for h in range(4):
            for i in range(9):
                for j in range(9):
                    for k in range(1,10):
                        user_row = i
                        user_column = j
                        user_number = k
                        options = ['options']
                        check_options()
                        lst = []
                        run_script(user_row, user_column)
                        if len(lst) == 4 and len(options) == 1:
                            sudoku[user_row][user_column] = user_number
        for i in sudoku:
            print(i)

    if user_choice == 'exit' or user_choice == 'finish':
        print('\nThanks for playing!')
        break

    if result:
        check_options()
        lst = []
        run_script(user_row, user_column)

    # Return True for five components to pull through and place the user_number
    if len(lst) == 4 and len(options) == 1:
        sudoku[user_row][user_column] = user_number
        print('\nGreat input!\n')
    else:
        strikes.append('x')
        if len(strikes) == 3:
            print("\nYou've got 3 strikes! you're out!\n")
            break
        else:
            print('\nWrong answer buddy\n')