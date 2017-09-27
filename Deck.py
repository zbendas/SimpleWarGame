from Card import Card
from Player import Player
import random


class Deck:
    def __init__(self):
        self.cardList = []
        for suit in ["C", "D", "H", "S"]:
            for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                self.cardList.append(Card(suit, rank))

    def __str__(self):
        printable = ""
        for index, card in enumerate(self.cardList):
            printable += str(card) + "\t"
            if index == 12 or index == 25 or index == 38:
                printable += "\n"
        return printable

    def shuffle(self):
        random.shuffle(self.cardList)

    def dealOne(self, player: Player):
        player.hand.append(self.cardList.pop(0))
        player.handNotEmpty = True


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print("\n\n")
    deck.shuffle()
    print(deck)
