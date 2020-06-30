import random


# Write your game of chance functions here
def flip_coin(bet, result):
    # Heads = 0
    # Tails = 1

    # Verify conditions to bet
    if bet > money:
        print("You don't have all that money to bet.")
        return 0
    if (result.lower() != "heads") and (result.lower() != "tails"):
        print("Invalid input result.")
        return 0

    print("You pick: " + result)
    event = random.randint(0, 1)

    if event == 0:
        print("Turned: Heads!")
    else:
        print("Turned: Tails!")

    if event == 0:
        if result.lower() == "heads":
            print("Congrats!!")
            return bet
        else:
            print("Better luck next time. :(")
            return -bet
    else:
        if result.lower() == "tails":
            print("Congrats!!")
            return bet
        else:
            print("Better luck next time. :(")
            return -bet

