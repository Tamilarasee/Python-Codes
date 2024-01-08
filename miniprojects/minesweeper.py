# commandline version of minesweeper games
import random
import re


class Grid:
    def __init__(self, grid_size, bombs_count):
        self.grid_size = grid_size
        self.bombs_count = bombs_count

        # create the grid
        self.grid = self.create_grid()

        # for every slot - store number of neighboring bombs in its immediate 3*3 grid
        self.store_neigh_bombs()


        # keep track of visible slots location(x,y)
        self.seen = set()

    def create_grid(self):
        # construct a new square grid - lists of lists
        grid = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.bombs_count:
            # randomly choose location to plant bombs -
            # consider like we numbered each slot of grid from 0.--->num of slots = size*size
            location = random.randint(0, self.grid_size ** 2 - 1)
            # find row/col from the chosen slot number
            row = location // self.grid_size
            col = location % self.grid_size

            # since we are using random numbers, we may get same number twice, so check if that location already has bomb and proceed
            if grid[row][col] == '*':
                continue

            grid[row][col] = '*'
            bombs_planted += 1

        return grid

    def store_neigh_bombs(self):
        # for every slot - store number of neighboring bombs in its immediate 3*3 grid

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # if it is bomb,leave that slot
                if self.grid[row][col] == '*':
                    continue

                self.grid[row][col] = self.get_neigh_bombs(row, col)

    def get_neigh_bombs(self, row, col):
        # Iterate through neighboring locations - the 3*3 grid (unless it is first or last row/col)
        # this virtual 3*3 grid is actually referring to one row above and below and one col left and right
        # to handle first or last row/col, use min/max in range function

        neigh_bombs_count = 0
        for r in range(max(0, row - 1), min(self.grid_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.grid_size - 1, col + 1) + 1):
                # needn't check current location - we checked it already before in store_neigh_bombs
                if r == row and c == col:
                    continue
                if self.grid[r][c] == '*':
                    neigh_bombs_count += 1
        return neigh_bombs_count

    def dig(self, row, col):

        # keep track of seen slots
        self.seen.add((row, col))
        print(self.seen)

        # bomb selection
        if self.grid[row][col] == '*':
            return False  # Game over

        # if there are bombs in neighboring slots, don't dig anymore - stop there
        elif self.grid[row][col] > 0:
            return True  # Game exists

        # if there are no neighboring bombs, uncover its immediate 3*3 grid (2 for loops) and
        # recurse to dig more slots until we see a slot with neighboring bombs

        for r in range(max(0, row - 1), min(self.grid_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.grid_size - 1, col + 1) + 1):
                if (r, c) in self.seen:
                    continue
                self.dig(r, c)  # this recursion breaks when it meets a bomb (return false) then,next iteration continues

        return True  # Game exists

    def __str__(self):
        # function definition to say what to return when "print" is called in this object
        # show the current grid to player

        # create a new 2D array of what user sees
        visible_board = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for row in range(self.grid_size):
            for col in range(self.grid_size):


                if (row, col) in self.seen:
                    visible_board[row][col] = str(self.grid[row][col])
                else:
                    visible_board[row][col] = " "


        # make a string with all values to print

        print("\n Current state\n")

        print("  ", end="")
        for i in range(self.grid_size):
            print(f" {i} ", end="")
        print("\n-----------------------------------")
        col = -1
        for row in ([visible_board[r][c] for c in range(len(visible_board))] for r in range(len(visible_board))):
            col += 1
            print(str(col) + ' |' + ' |'.join(row) + ' |')


        return ''


# prepare the grid and play
def mines_play(grid_size=10, bombs_count=10):
    # create the grid and plant the bombs
    grid = Grid(grid_size, bombs_count)
    # print the grid and get input from user to dig

    # game over - if the location is bomb

    # dig recursively until the invisible slots are only bombs - if not bomb

    # repeat until every slot is visible
    game = True
    while len(grid.seen) < (grid.grid_size ** 2 - bombs_count):
        print(grid)
        # re is used to handle cases like (0,0)  (0, 0)  (0,   0) - just handling any space after ,
        choice = re.split(',(\\s)*', input("Input row,column to dig: "))
        row = int(choice[0])
        col = int(choice[-1])

        if row not in range(grid_size) or col not in range(grid_size) or (row,col) in grid.seen:
            print("Invalid selection. Try again")
            continue

        # for valid selection, begin the game
        game = grid.dig(row, col)

        if not game:
            # A bomb was selected - Game over!
            break

    if game:
        print("Yay!!...You won😎")
    else:
        print("Sorry! Game over :(")
    grid.seen = [(r, c) for r in range(grid.grid_size) for c in range(grid.grid_size)]
    print(grid)


if __name__ == '__main__':
    mines_play()
