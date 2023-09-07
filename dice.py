import random
import time

def roll_dice():
    dice_faces = [
        [
            "+-------+",
            "|       |",
            "|   *   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *     |",
            "|       |",
            "|     * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *     |",
            "|   *   |",
            "|     * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *   * |",
            "|       |",
            "| *   * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *   * |",
            "|   *   |",
            "| *   * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *   * |",
            "| *   * |",
            "| *   * |",
            "+-------+"
        ]
    ]
    
    print("Rolling the dice...")
    
    for _ in range(8):  # Number of spins
        roll = random.randint(1, 6)
        print("\033c")  # Clear console screen
        print(*dice_faces[roll - 1], sep='\n')
        print(f"The dice rolled: {roll}")
        time.sleep(0.36)  # Delay between spins
    
    print("\033c")  # Clear console screen
    print(*dice_faces[roll - 1], sep='\n')
    print(f"The final dice roll: {roll}")

roll_dice()
