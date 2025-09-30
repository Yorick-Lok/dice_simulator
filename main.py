from random import randint

def dice_amount():
    """Ask how many dice the user wants to roll. Must be between 3 and 5."""
    while True:
        try:
            amount_input = input("""How many dice would you like to roll? (3-5)
Type q to quit.\n""")
            if amount_input == 'q':
                exit()  # Quit if the user sends 'q'
            else:
                amount = int(amount_input)  # Turn the user input into an integer.
            if 3 <= amount <= 5:
                print("You entered:", amount)
                return amount  # Return the integer.
            else:
                print("Invalid Input. Please enter a number between 3 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def dice_roll(num_dice):
    """Rolls 'num_dice' dice and prints the results."""
    print(f"\nRolling {num_dice} dice...")
    results = []
    bottom_results = []
    six_rolls = 0  # Move this outside the loop

    for i in range(1, num_dice + 1):
        rolled_number = randint(1, 6)
        results.append(rolled_number)

        bottom_rolled_number = 7 - rolled_number
        bottom_results.append(bottom_rolled_number)

        print(f"Dice {i}: {rolled_number}")
        print(f"Bottom of Dice {i}: {bottom_rolled_number}")

        if rolled_number == 6:
            six_rolls += 1

    # After all dice are rolled, check for 3 or more sixes
    if six_rolls >= 3:
        print(f"\nYou rolled a six {six_rolls} times!")

    return results, bottom_results


def total_count(rolls, bottom_rolls):
    """Determines the number the dice add up to."""
    print("\nAdding up the rolled numbers...")
    total = sum(rolls)
    bottom_total = sum(bottom_rolls)
    print(f"Your dice add up to: {total}")
    print(f"The bottom of your dice add up to: {bottom_total}")

def play_game():
    """Main Game Loop."""
    while True:
        dice_count = dice_amount()
        rolled_dice, bottom_dice = dice_roll(dice_count)
        total_count(rolled_dice, bottom_dice)

        while True:
            again = input("Would you like to play again? (y/n)\n")
            if again == 'y':
                print("\n" + "-" * 30 + "\n")
                break  # Break the inner loop and start a new game
            elif again == 'n':
                print("Thanks for playing!")
                return  # Exit the function, ending the game
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


# Run the game
play_game()
