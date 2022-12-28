import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter palyer 1's name ")
    player2 = input("Enter palyer 2's name ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print("Player1", roll1)
    print("Player2", roll2)

    if roll1 > roll2:
        print("Player1 wins!")
    elif roll2 > roll1:
        print("Player2 wins!")
    else:
        print("Its tie!")

main()
