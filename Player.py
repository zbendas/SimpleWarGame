class Player:
    def __init__(self):
        self.hand = []
        self.handTotal = 0
        self.handNotEmpty = False

    def __str__(self):
        printable = ""
        for index, card in enumerate(self.hand):
            printable += str(card) + "\t"
            if index == 12 or index == 25 or index == 38:
                printable += "\n"
        return printable
