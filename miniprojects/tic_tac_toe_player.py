import math
import random


# Parent class
class Player:
    def __init__(self, letter):
        self.letter = letter

    def make_choice(self, game):
        pass


class Random_Computer(Player):
    def __init(self, letter):
        super().__init__(letter)

    def make_choice(self, game):
        print("\n🤔")
        computer_choice = random.choice(game.empty_slots())
        return computer_choice


class User(Player):
    def __init(self, letter):
        super().__init__(letter)

    def make_choice(self, game):
        valid_input = False
        while not valid_input:
            user_choice = input(f'\n{self.letter}\'s turn. Input available choice from the grid (0 to 8)')
            try:
                user_choice = int(user_choice)
                if user_choice not in game.empty_slots():
                    raise ValueError
                valid_input = True
            except ValueError:
                print("Invalid Input. Try again")
        return user_choice


class Super_Computer(Player):
    def __init(self, letter):
        super().__init__(letter)

    def make_choice(self, game):
        if len(game.empty_slots()) == 9:
            super_computer_choice = random.choice(game.empty_slots())
        else:
            # call minimax algorithm to find the best slot
            choice = self.minimax(game, self.letter)
            super_computer_choice = choice['slot']
        return super_computer_choice

    def minimax(self, state, player1):
        max_player = self.letter  # Super_Computer's letter
        player2 = 'O' if player1 == 'X' else 'X'  # Alternate players everytime this function is called

        # Basecase - we stop algorithm if someone wins or the game is a tie
        # In the previous trial, if the game was won on result of player2 move, then generate the slot and score
        # If the super_computer won in the previous call, we consider +1 else, -1 (loss for super_computer)
        # we use number of empty slots as parameter for calculation of score, as we want to win the game in less moves
        # which means more empty slots left
        if state.win == player2:
            return {'slot': None,
                    'score': 1 * (len(state.empty_slots()) + 1) if player2 == max_player else -1 * (len(state.empty_slots()) + 1)}
        # If there are no empty slots, we are not going to move anywhere and hence no score calculation as well
        elif not state.empty_slots():
            return {'slot': None,
                    'score': 0}

        if player1 == max_player:
            best = {'slot': None,
                    'score': -math.inf}  # keep it lowest in beginning so we can maximize at every iteration
        else:
            best = {'slot': None,
                    'score': math.inf}  # keep it largest in beginning so we can minimize at every iteration

        # logic
        for trial_slot in state.empty_slots():
            # step1 - Try a slot from available options - Player1 makes the move
            state.grid[trial_slot] = player1
            state.winner(trial_slot, player1)
            # step2 - Recursive minimax,to simulate the game based on chosen trial slot (filling in a branch - top to bottom)
            # and calculate score/slot to see if there is an improvement-- repeat the function for the next player
            trial_score = self.minimax(state, player2)
            # Step 3 - Undo the move & winner to do the next trial (next branch)
            state.grid[trial_slot] = ' '
            state.win = None
            trial_score['slot'] = trial_slot  # at the end of the game , update the slot originally started for this particular trial tree
            # Step 4 - Update the dict with slots/scores as necessary
            # Maximize max_player and minimize the min player
            if player1 == max_player:
                if trial_score['score'] > best['score']:
                    best = trial_score
            else:
                if trial_score['score'] < best['score']:
                    best = trial_score

        return best
