import random


# Write your game of chance functions here
def flip_coin(bet, result):
    # Heads = 0
    # Tails = 1
    print('''##########
FLIP COIN 
##########''')

    # Verify conditions to bet
    if bet > money or bet < 0:
        print("You don't have all that money to bet.\n")
        return 0
    if (result.lower() != "heads") and (result.lower() != "tails"):
        print("Invalid input result.\n")
        return 0

    print("You pick: " + result)
    event = random.randint(0, 1)

    if event == 0:
        print("Turned: Heads!")
    else:
        print("Turned: Tails!")

    if event == 0:
        if result.lower() == "heads":
            print("Congrats you win!!\n")
            return bet
        else:
            print("Better luck next time. :(\n")
            return -bet
    else:
        if result.lower() == "tails":
            print("Congrats you win!!\n")
            return bet
        else:
            print("Better luck next time. :(\n")
            return -bet


def cho_han(bet, result):
    print('''##########
CHO    HAN 
##########''')

    # Verify conditions to bet
    if bet > money or bet < 0:
        print("You don't have all that money to bet.\n")
        return 0
    if (result.lower() != "odd") and (result.lower() != "even"):
        print("Invalid input result.\n")
        return 0

    print("You picked a result of sum the dices: " + result)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    event = dice1 + dice2
    print("Sum the dices is: " + str(event))

    if (event % 2) == 0:
        if result.lower() == "even":
            print("Congrats you win!!\n")
            return bet
        else:
            print("Better luck next time. :(\n")
            return -bet
    else:
        if result.lower() == "odd":
            print("Congrats you win!!\n")
            return bet
        else:
            print("Better luck next time. :(\n")
            return -bet


def pick_card(bet):
    print('''##########
PICK  CARD 
##########''')

    # Verify conditions to bet
    if bet > money:
        print("You don't have all that money to bet.\n")
        return 0

    # Start variables
    event1_value = 0
    event2_value = 0

    deck = [2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,
            "J", "J", "J", "J",
            "Q", "Q", "Q", "Q",
            "K", "K", "K", "K",
            "A", "A", "A", "A"]

    # Draw first card
    event1 = random.randint(0, 51)
    print("Your card is: " + str(deck[event1]))
    if deck[event1] == "J":
        event1_value = 11
    elif deck[event1] == "Q":
        event1_value = 12
    elif deck[event1] == "K":
        event1_value = 13
    elif deck[event1] == "A":
        event1_value = 14
    else:
        event1_value = deck[event1]
    # Remove it from the deck
    deck.pop(event1)
    # Print card infos
    print("The value of your card is: " + str(event1_value))

    print()

    # Draw second card
    event2 = random.randint(0, 50)
    print("The opponent's card is: " + str(deck[event2]))
    if deck[event2] == "J":
        event2_value = 11
    elif deck[event2] == "Q":
        event2_value = 12
    elif deck[event2] == "K":
        event2_value = 13
    elif deck[event2] == "A":
        event2_value = 14
    else:
        event2_value = deck[event2]
    # Remove it from the deck
    deck.pop(event2)
    # Print card infos
    print("The value of his card is: " + str(event2_value))

    # Compare results
    if event1_value == event2_value:
        print("There is a tie!\n")
        return 0
    elif event1_value > event2_value:
        print("Congrats you win!!\n")
        return bet
    else:
        print("Better luck next time. :(\n")
        return -bet


# Call your game of chance functions here
money = 100
print(money)
print()
money += flip_coin(20, "heads")
money += cho_han(20, "even")
money += pick_card(50)
print(money)
