from tic_tac_toe_player import User, Random_Computer,Super_Computer


class TicTacToe:
    def __init__(self):
        self.grid = [' ' for i in range(9)]
        self.win = None

    def grid_structure(self):
        # display of the grid
        for row in ([self.grid[i * 3:(i + 1) * 3] for i in range(3)]):
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def grid_numbers():
        # This is used only once at the beginning of the game to show the user the number places
        grid_numbers = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in grid_numbers:
            print('|' + '|'.join(row) + '|')

    def empty_slots(self):
        # the indexes of emplty slots at any point of time
        empty_slots = [i for i, slot in enumerate(self.grid) if slot == ' ']
        return empty_slots

    def winner(self, slot, letter):
        # Row - find row 0,1,2 based on the slot where the last letter was entered and then validate
        row_index = slot // 3
        row = self.grid[row_index * 3:(row_index + 1) * 3]
        if all([space == letter for space in row]):
            self.win=letter
            return True
        # Col - find Col 0,1,2 based on the slot where the last letter was entered and then validate
        col_index = slot % 3
        col = [self.grid[col_index + i * 3] for i in range(3)]
        if all([space == letter for space in col]):
            self.win=letter
            return True
        # Check diagonals
        diagonal1 = [0, 4, 8]
        diagonal2 = [2, 4, 6]
        if slot in diagonal1 or slot in diagonal2:
            if all([self.grid[space] == letter for space in diagonal1]) or all(
                    [self.grid[space] == letter for space in diagonal2]):
                self.win = letter
                return True
        return False


def tic_tac_toe_play(game, x_player, o_player):
    print("\nRefer to below grid for numbers\n")
    game.grid_numbers()
    # Starting the game with X always
    letter = 'X'
    # Loop until all slots are filled or break if someone wins
    while game.empty_slots():

        if letter == 'X':
            slot = x_player.make_choice(game)
        else:
            slot = o_player.make_choice(game)
        game.grid[slot] = letter
        print(f'\n{letter} makes a move to slot {slot}\n')
        game.grid_structure()
        # Check if there is a winner after every move
        if game.winner(slot, letter):
            print(f'\n{letter} wins!🥳\n')
            break
        # Alternate the players after every move
        letter = 'O' if letter == 'X' else 'X'
    else:
        print("\nIt\'s a tie!\n")


if __name__ == "__main__":
    print("Lets begin the game")
    while True:
        choice = input("Play/Quit - Press P/Q: ").lower()
        if choice == 'p':
            opponent = input("Whom do you want to play against? \n1. Random Computer \n2. Super Computer\n\nYour opponent: ")
            letter = input("What do you prefer X/O? ").upper()
            if letter == 'X':
                x_player = User('X')
                if opponent == '1':
                    o_player = Random_Computer('O')
                elif opponent == '2':
                    o_player = Super_Computer('O')
                else:
                    print("Invalid choice of opponent")
            elif letter == 'O':
                o_player = User('O')
                if opponent == '1':
                    x_player = Random_Computer('O')
                elif opponent == '2':
                    x_player = Super_Computer('O')
                else:
                    print("Invalid choice of opponent")
            else:
                print("Invalid input of letter")
                continue
            game = TicTacToe()
            tic_tac_toe_play(game, x_player, o_player)
        elif choice == 'q':
            print("Thanks for playing 😇")
            break
        else:
            print("Invalid input")
