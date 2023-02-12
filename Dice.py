import random

def dice():
    drawing_of_dice = {
        1: (
            "|=======|",
            "|    ◉1    |",
            "|=======|",
        ),
        2: (
            "|=======|",
            "| ◉  2    |",
            "|        ◉ |",
            "|=======|",
        ),
        3: (
            "|========|",
            "| ◉     3   |",
            "|      ◉     |",
            "|           ◉|",
            "|========|",
        ),
        4: (
            "|=======|",
            "| ◉ 4 ◉ |",
            "| ◉    ◉ |",
            "|=======|",
        ),
        5: (
            "|========|",
            "| ◉   5  ◉|",
            "|      ◉     |",
            "| ◉      ◉ |",
            "|========|",
        ),
        6: (
            "|========|",
            "| ◉      ◉ |",
            "| ◉   6 ◉ |",
            "| ◉      ◉ |",
            "|========|",
        ),
    }
    dice_roll = input("roll the dice? (y/n): ")
    
    while dice_roll.upper() == "y".upper():
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        
        print("Rolling dice: {} and {}".format(roll1, roll2))
        print("\n".join(drawing_of_dice[roll1]))
        print("\n".join(drawing_of_dice[roll2]))
        
        dice_roll = input("Rolling dice again? (y/n): ")
        
dice()
        