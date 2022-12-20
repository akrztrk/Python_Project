import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      "Rock vs paper->paper wins \n"
      "Rock vs scissor->Rock wins \n"
      "paper vs scissor->scissor wins")

while True:
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors: \n"))
    # I wanted the user to choose a number between 0 and 2 and converted it to an integer.
    computer_choice = random.randint(0, 2)
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose")
    elif computer_choice == 2 and user_choice == 0:
        print("You wins")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice < user_choice:
        print("You wins")
    elif computer_choice == user_choice:
        print("It's draw")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break