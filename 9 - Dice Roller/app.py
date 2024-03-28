import random

def roll_dice(num_dice, num_sides):
    """
    Rolls the specified number of dice with the specified number of sides.
    Returns a list of the individual dice rolls.
    """
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

def main():
    while True:
        num_dice = input("How many dice would you like to roll? (Enter 'q' to quit): ")
        if num_dice.lower() == 'q':
            break

        try:
            num_dice = int(num_dice)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        num_sides = input(f"How many sides per die? (Default is 6): ") or "6"
        try:
            num_sides = int(num_sides)
        except ValueError:
            print("Invalid input. Using default of 6 sides.")
            num_sides = 6

        rolls = roll_dice(num_dice, num_sides)
        print(f"You rolled: {', '.join(str(roll) for roll in rolls)}")
        print(f"Total: {sum(rolls)}")

if __name__ == "__main__":
    main()