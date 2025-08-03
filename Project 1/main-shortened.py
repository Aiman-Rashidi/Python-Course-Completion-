# | Move      | Code |
# | ----------| ---- |
# |  Stone    | -1   |
# |  Paper    | 0    |
# |  Scissors | 1    |

import random

computer_choice = random.choice([-1, 0, 1])
user_choice = int(input("(\"stone\": -1, \"paper\": 0, \"scissors\": 1): "))

choice_map = {-1: "stone", 0: "paper", 1: "scissors"}
print(f"Your choice: {choice_map[user_choice]} & Computer's choice: {choice_map[computer_choice]}")

if computer_choice == user_choice:
    print("Draw!")
else:
    # if computer_choice == -1 and user_choice == 0:      #(computer_choice - user_choice) == -1
    #     print("Win!")
    # elif computer_choice == -1 and user_choice == 1:    #(computer_choice - user_choice) == -2
    #     print("Lose!")
    # elif computer_choice == 0 and user_choice == -1:    #(computer_choice - user_choice) == 1
    #     print("Lose!")
    # elif computer_choice == 0 and user_choice == 1:     #(computer_choice - user_choice) == -1
    #     print("Win!")
    # elif computer_choice == 1 and user_choice == -1:    #(computer_choice - user_choice) == 2
    #     print("Win!")
    # elif computer_choice == 1 and user_choice == 0:     #(computer_choice - user_choice) == 1
    #     print("Lose!")
    # else:
    #     print("something went wrong!")
        
    # The below logic is written on the basis of the value of (computer_choice - user_choice)

    if (computer_choice - user_choice == -1) or (computer_choice - user_choice == 2):
        print("Win!")
    elif (computer_choice - user_choice == -2) or (computer_choice - user_choice == 1):
        print("Lose!")
    else:
        print("something went wrong!")