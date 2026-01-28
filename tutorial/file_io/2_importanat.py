import random 
#generating a game
def game():
    score = random.randint(1,100)

    with open("hiscore.txt") as f:
        hiscore =f.read()
        if (hiscore != " "):
            hisocre = int(hiscore)
        else:
            print("hiscore is 0")

    print("your hiscore is :", score)

    if (score>hiscore):
        with open ("hiscore.txt" , "w") as f:
            f.write(str(score))
    return score
game()

