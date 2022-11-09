import random

range_max = 10
turns_count = 3

decision_list = ["YES", "Y", "YE"]
number_list = range(range_max + 1)
decision = "YES"
print(
    "Let's play! I will think of a number from 0 to 10 and you will have to guess what the number is. If you guess on your first try, you get 10 points.\n"
    "If not, you will have your second try, but this time only for 5 points. If you don't guess the number, you will get no points.\n"
    "There will be three separate rounds in total. If you manage to score at least 15 points, you win! Let us begin...")
# start of the game
while decision in decision_list:
    score = 0
    for i in range(1, turns_count + 1):
        prize = 10
        print(f"Turn {i}")
        computer_choice = random.randint(0, range_max)
        guess_numeric = -1
        second_guess_numeric = -1

        for j in range(2):
            wrong_input = True
            # input validation
            while wrong_input:
                guess = (input("Guess what number from 0 to 10 I'm thinking of!"))
                if guess.isnumeric():
                    guess_numeric = int(guess)
                    if guess_numeric in number_list:
                        wrong_input = False
                    else:
                        print("That's not a number between 0 and 10. Try again.")
                else:
                    print("That's not a number! Try again.")

            # checking if the guess = computer choice
            if guess_numeric == computer_choice:
                score = score + prize
                print(f"Correct! You have {score} points!")
                continue
            elif prize == 10:  # first chance miss
                if guess_numeric < computer_choice:
                    print("Wrong, it is a bigger number. Let's try one more time.")
                elif guess_numeric > computer_choice:
                    print("Wrong, it is a smaller number. Let's try one more time.")
                prize = 5
            else:  # second chance miss
                print(f"Unfortunately, that's not that one either. Your score is {score}.")

    # final score
    if score < 15:
        print(f"Sorry, you lose! Your final score is {score} points.")
    else:
        print(f"Congratulations! You won! Your final score is {score} points.")
    decision = input("Do you want to play again? Type yes or no.").upper()
