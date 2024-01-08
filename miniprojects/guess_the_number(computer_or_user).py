import random
def guess_game_user(start, end, attempt):
    secret_number = random.randint(start, end)
    num_guess = 1
    while num_guess <= attempt:
        user_guess = int(input(f"Guess a number between {start} and {end}: "))
        if secret_number == user_guess:
            print(f'Congrats! You guessed the number {secret_number} correctly')
            break
        elif secret_number > user_guess:
            print("Your guess is low")
            num_guess += 1
        elif secret_number < user_guess:
            print("Your guess is high")
            num_guess += 1
    else:
        print("Thank you for playing!!!")

def guess_game_computer(start,end,attempt):
    num_guess = 1
    while num_guess <= attempt:
        computer_guess = random.randint(start, end)
        feedback = input(f"My guess is {computer_guess}.Please input (L/H/C) if my number is low, high or correct: ")
        if feedback.upper() == 'C':
            print(f'Yay! I guessed the number {computer_guess} correctly')
            break
        elif feedback.upper() == 'L':
            start = computer_guess+1
            num_guess += 1
        elif feedback.upper() == 'H':
            end = computer_guess-1
            num_guess += 1
    else:
        print("You win! Thank you for playing!!!")


print("Welcome to guessing game")
player = input("Who would like to guess? User/Computer? ")
print("Rules for game:")
start = int(input("What is the minimum number? "))
end = int(input("What is the maximum number? "))
attempt = int(input("No.of allowed attempts? "))
print("Let's begin")
if player =="User":
    guess_game_user(start,end,attempt)
elif player == "Computer":
    print("Think of a secret number in your mind and give me feedback on my guess")
    guess_game_computer(start,end,attempt)

