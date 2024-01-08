import random

def play_rps(matches,won,lost):

    computer = random.choice(['r', 'p', 's'])
    print(computer)
    user = input("Enter R for Rock, P for Paper and S for Scissors: ").lower()

    if user not in ('r', 'p', 's'):
        print("Invalid input")
        exit()
    matches += 1
    if user == computer:
        print("Its a draw")
    else:
        won,lost = game_result(user,computer,won,lost)
    return matches,won,lost

def game_result(user,computer,won,lost):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or \
            (user == 's' and computer == 'p' ):
        print("You win!")
        won+=1
    else:
        print("You lost!")
        lost+=1
    return won,lost

if __name__ == "__main__" :
    matches,won,lost = 0,0,0
    print("Lets begin the game")
    while(True):
        choice = input("Play/Quit - Press P/Q: ").lower()
        if choice =='p':
            matches,won,lost = play_rps(matches,won,lost)
        elif choice =='q':
            print(f"Number of matches played: {matches} \nNumber of games Won: {won} \nNumber of games lost: {lost}")
            print("Thanks for playing!!!")
            break
        else:
            print("Invalid input")




