from random import randint

def game():
    print("you are palying the game...")
    score = randint(1, 100)
    print(f"Your Score: {score}")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    if hiscore != "":
        hiscore = int(hiscore)
    else:
        hiscore = 0

    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()