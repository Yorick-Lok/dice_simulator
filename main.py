from random import randint

def dice_amount():
    """Ask how many dice the user wants to roll. Must be between 3 and 5."""
    while True:
        # Ask for a number ranging from 3 to 5.
        try:
            amount_input = input("""How many dice would you like to roll? (3-5)
Type q to quit.\n""")
            if amount_input == 'q':
                exit() # Quit if the user sends Q
            else:
                amount = int(amount_input) # Turn the user input into an integer.
            if 3 <= amount <= 5:
                print("You entered:", amount)
                return amount # Return the integer.
            else: # Return an error.
                print("Invalid Input. Please enter a number between 3 and 5.")
        except ValueError: # Return an error.
            print("Invalid input. Please enter a number.")

def dice_roll(num_dice):
    """Rolls 'num_dice' dice and prints the results."""
    print(f"\nRolling {num_dice} dice...")
    results = []
    for i in range(1, num_dice + 1):
        rolled_number = randint(1, 6)
        print(f"Dice {i}: {rolled_number}")
        results.append(rolled_number) # Print a randomly generated number ranging from 1 to 6.
    return results

def total_count(rolls):
    """Determines the number the dice add up to."""
    print("\nAdding up the rolled numbers...")
    total = sum(rolls)
    print(f"Your dice add up to: {total}")

def play_game():
    """Main Game Loop."""
    while True:
        dice_count = dice_amount()
        rolled_dice = dice_roll(dice_count)
        total_count(rolled_dice)

        again = input("Would you like to play again? (y/n)\n")
        if again != 'y':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
