from Deck import Deck
from Player import Player
import random


ties = 0
nested_ties = 0


def main():
    cardDeck = Deck()
    print("Initial deck:")
    print(cardDeck)

    random.seed(16)
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)

    player1 = Player()
    player2 = Player()

    for i in range(26):
        cardDeck.dealOne(player1)
        cardDeck.dealOne(player2)

    playGame(cardDeck, player1, player2)

    if player1.handNotEmpty:
        print("\n\nGame over. Player 1 wins!")
    else:
        print("\n\nGame over. Player 2 wins!")

    print("\n\nFinal hands:")
    print("Player 1:\t")
    print(player1)
    print("\nPlayer 2:")
    print(player2)
    print("Resolved {0} ties.".format(ties))
    print("Resolved {0} nested ties.".format(nested_ties))


def resolve_tie(player1, player2, card1, card2):
    print("Resolving tie")
    global ties
    global nested_ties
    ties += 1
    cards_at_stake1 = []
    cards_at_stake2 = []
    for i in range(3):
        try:
            cards_at_stake1.append(player1.hand.pop(0))
        except IndexError:
            player1.handNotEmpty = False
            player2.hand.append(card1)
            player2.hand.append(card2)
            for card in cards_at_stake1:
                player2.hand.append(card)
            for card in cards_at_stake2:
                player2.hand.append(card)
            return
        try:
            cards_at_stake2.append(player2.hand.pop(0))
        except IndexError:
            player2.handNotEmpty = False
            player1.hand.append(card1)
            player1.hand.append(card2)
            for card in cards_at_stake1:
                player1.hand.append(card)
            for card in cards_at_stake2:
                player1.hand.append(card)
            return
    try:
        card3 = player1.hand.pop(0)
    except IndexError:
        player1.handNotEmpty = False
        player2.hand.append(card1)
        player2.hand.append(card2)
        for card in cards_at_stake1:
            player2.hand.append(card)
        for card in cards_at_stake2:
            player2.hand.append(card)
        return
    try:
        card4 = player2.hand.pop(0)
    except IndexError:
        player2.handNotEmpty = False
        player1.hand.append(card1)
        player1.hand.append(card2)
        for card in cards_at_stake1:
            player1.hand.append(card)
        for card in cards_at_stake2:
            player1.hand.append(card)
        player1.hand.append(card3)
        return
    if card3 > card4:
        player1.hand.append(card1)
        player1.hand.append(card2)
        for card in cards_at_stake1:
            player1.hand.append(card)
        for card in cards_at_stake2:
            player1.hand.append(card)
        player1.hand.append(card3)
        player1.hand.append(card4)
    elif card3 < card4:
        player2.hand.append(card1)
        player2.hand.append(card2)
        for card in cards_at_stake1:
            player2.hand.append(card)
        for card in cards_at_stake2:
            player2.hand.append(card)
        player2.hand.append(card3)
        player2.hand.append(card4)
    else:
        nested_ties += 1
        resolve_tie(player1, player2, card3, card4)


def playGame(deck, player1, player2):
    print("Playing the game.")
    while len(player1.hand) > 0 and len(player2.hand) > 0:
        print("Playing a new turn.")
        print(str(len(player1.hand)) + "\t" + str(len(player2.hand)))
        card1 = player1.hand.pop(0)
        card2 = player2.hand.pop(0)
        if card1 == card2:
            resolve_tie(player1, player2, card1, card2)
        elif card1 > card2:
            player1.hand.append(card1)
            player1.hand.append(card2)
        elif card1 < card2:
            player2.hand.append(card1)
            player2.hand.append(card2)


if __name__ == "__main__":
    main()
