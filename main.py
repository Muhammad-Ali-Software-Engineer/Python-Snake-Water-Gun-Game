"""
Snake, Water, Gun Game
snake = 1
water = -1
gun = 0
"""
import random
computer_choice = random.choice([-1, 0, 1])
user_input = input("Enter choice (s = Snake, w = Water, g = Gun): ").lower()

choice_map = {
    "s": 1,
    "w": -1,
    "g": 0 
}
reverse_choice_map = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}
user_choice = choice_map[user_input]
print(f"You chose {reverse_choice_map[user_choice]}")
print(f"Computer chose {reverse_choice_map[computer_choice]}")

if computer_choice == user_choice:
    print("It's a draw!")
else:
    if computer_choice == 1 and user_choice == -1:
        print("You win!")
    elif computer_choice == 1 and user_choice == 0:
        print("You lose!")
    elif computer_choice == -1 and user_choice == 1:
        print("You lose!")
    elif computer_choice == -1 and user_choice == 0:
        print("You win!")
    elif computer_choice == 0 and user_choice == 1:
        print("You win!")
    elif computer_choice == 0 and user_choice == -1:
        print("You lose!")
    else:
        print("Something went wrong.")

    """*************************************************
        Congratulations first game in python done
    *************************************************"""