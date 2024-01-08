# we input a sudoku puzzle. The program solves it if possible and prints the solution

def empty_slots(puzzle):
    #finding the slot that is not given any value - we fix such slots to be -1
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c  #this returns a tuple (r,c) of th empty slot

    return None,None   #this is when all slots are filled

def is_valid(puzzle,value,row,col):
    #check if the value at row,col meets the rules at current condition of puzzle
    #as per rules, a value should not be repeated in a row,col or in the 3x3 matrix

    row_values = puzzle[row]
    col_values = [puzzle[r][col] for r in range(9)]
    if value in row_values or value in col_values:
        return False

    #to find the small 3x3 grid, we find the starting row/col of the 3x3 block to find which block it belongs
    #then, iterate 3 rows down and 3 col right - check all 9 values of the block

    block_row = row//3 * 3
    block_col = col//3 * 3

    for r in range(block_row,block_row+3):
        for c in range(block_col,block_col+3):
            if puzzle[r][c] == value:
                return False

    return True  # if all above rules were not violated, the value is valid




#bactracking algorithm to find the right values
#This method says if this list of values form valid solution
def solve(puzzle):

    #Choose the starting point
    row,col = empty_slots(puzzle)

    #base case
    if row is None:
        return True     #puzzle solved - all slots are filled (we allow only valid values to be filled as per logic)

    #If there is empty slot, fill it with a valid value(1 to 9) - try each value and see if game conditions are satisfied
    for value in range(1,10):
        if is_valid(puzzle,value,row,col):
            puzzle[row][col] = value  #place it in the puzzle

            if solve(puzzle): #recurse the function untill all rows are filled and then return True - which means puzzle is solvable and we solved it
                return True

        #what if we choose a valid value for that 3x3 but later that clashes with future empty position value and you end up having no valid value?
        #In this situation, we change our old position value and try a new value to see if this opens up a new possible valid value in other empty position
        puzzle[row][col] = -1  #reset the value, take a step back and try a new value from for loop and then recurse again

    #if none of the combinations work for every single slot for every 1 to 9 numbers, then this puzzle is not solvable - return False
    return False

if __name__ == "__main__":
    puzzle = [
        [8, -1, -1, -1, -1, -1, -1, 4, -1],
        [3, -1, -1, 8, -1, -1, 5, 6, -1],
        [-1, -1, 2, -1, -1, 3, -1, -1, -1],

        [5, -1, -1, -1, -1, -1, -1, -1, 4],
        [-1, -1, 7, -1, 6, -1, 9, 5, -1],
        [-1, -1, -1, 9, -1, -1, -1, -1, 2],

        [2, -1, -1, 6, -1, -1, 8, 3, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 9],
        [-1, 1, -1, -1, 7, -1, -1, -1, -1]
    ]
    if solve(puzzle):
        print("Yay! we have solved it! \n Here is the solution:\n")
        for row in ([str(puzzle[r][c]) for c in range(len(puzzle))] for r in range(len(puzzle))):
            print( ' |' + ' |'.join(row) + ' |')
    else:
        print("Invalid or Unsolvable puzzle")


