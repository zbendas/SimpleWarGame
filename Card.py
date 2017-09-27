class Card:
    def __init__(self, suit, rank):
        self.Suit = suit.upper()
        self.Rank = rank

    def __str__(self):
        return str(self.Suit) + str(self.Rank)

    def __lt__(self, other):
        if isinstance(other, Card):
            if other.Rank not in ["J", "Q", "K", "A"] and self.Rank not in ["J", "Q", "K", "A"]:
                if self.Rank < other.Rank:
                    return True
                else:
                    return False
            elif other.Rank in ["J", "Q", "K", "A"] and self.Rank not in ["J", "Q", "K", "A"]:
                return True
            elif self.Rank in ["J", "Q", "K", "A"] and other.Rank not in ["J", "Q", "K", "A"]:
                return False
            else:
                if other.Rank == "J":
                    return False
                elif (other.Rank == "Q" or other.Rank == "K" or other.Rank == "A") and self.Rank == "J":
                    return True
                elif (other.Rank == "K" or other.Rank == "A") and (self.Rank == "J" or self.Rank == "Q"):
                    return True
                elif (other.Rank == "A") and (self.Rank == "J" or self.Rank == "Q" or self.Rank == "K"):
                    return True
                else:
                    return False
        else:
            raise TypeError("Cannot compare to non-Card object.")

    def __le__(self, other):
        if isinstance(other, Card):
            if self < other or self == other:
                return True
            else:
                return False
        else:
            raise TypeError("Cannot compare to non-Card object.")

    def __eq__(self, other):
        if isinstance(other, Card):
            if self.Rank == other.Rank:
                return True
            else:
                return False
        else:
            raise TypeError("Cannot compare to non-Card object.")

    def __ne__(self, other):
        if isinstance(other, Card):
            if self.Rank != other.Rank:
                return True
            else:
                return False
        else:
            raise TypeError("Cannot compare to non-Card object.")

    def __gt__(self, other):
        if isinstance(other, Card):
            if other.Rank not in ["J", "Q", "K", "A"] and self.Rank not in ["J", "Q", "K", "A"]:
                if self.Rank > other.Rank:
                    return True
                else:
                    return False
            elif self.Rank in ["J", "Q", "K", "A"] and other.Rank not in ["J", "Q", "K", "A"]:
                return True
            elif other.Rank in ["J", "Q", "K", "A"] and self.Rank not in ["J", "Q", "K", "A"]:
                return False
            else:
                if other.Rank == "J" and (self.Rank == "Q" or self.Rank == "K" or self.Rank == "A"):
                    return True
                elif (other.Rank == "J" or other.Rank == "Q") and (self.Rank == "K" or self.Rank == "A"):
                    return True
                elif (other.Rank == "J" or other.Rank == "Q" or other.Rank == "K") and self.Rank == "A":
                    return True
                elif other.Rank == "A":
                    return False
                else:
                    return False

        else:
            raise TypeError("Cannot compare to non-Card object.")

    def __ge__(self, other):
        if isinstance(other, Card):
            if self > other or self == other:
                return True
            else:
                return False
        else:
            raise TypeError("Cannot compare to non-Card object.")


def compare_lt(first_card, second_card):
    print("Card1: {0}\tCard2: {1}".format(first_card, second_card))
    print(first_card < second_card)


def compare_le(first_card, second_card):
    print("Card1: {0}\tCard2: {1}".format(first_card, second_card))
    print(first_card <= second_card)


def compare_eq(first_card, second_card):
    print("Card1: {0}\tCard2: {1}".format(first_card, second_card))
    print(first_card == second_card)


def compare_ne(first_card, second_card):
    print("Card1: {0}\tCard2: {1}".format(first_card, second_card))
    print(first_card != second_card)


def compare_gt(first_card, second_card):
    print("Card1: {0}\tCard2: {1}".format(first_card, second_card))
    print(first_card > second_card)


def compare_ge(first_card, second_card):
    print("Card1: {0}\tCard2: {1}".format(first_card, second_card))
    print(first_card >= second_card)


def test_lt():
    print("-" * 10 + "\nLess Than\n" + "-" * 10)
    card1 = Card("C", 2)
    card2 = Card("H", 2)
    compare_lt(card1, card2)
    card2 = Card("H", 3)
    compare_lt(card1, card2)
    card2 = Card("H", "J")
    compare_lt(card1, card2)
    card1 = Card("C", "Q")
    card2 = Card("H", 2)
    compare_lt(card1, card2)
    card1 = Card("C", "J")
    card2 = Card("H", "J")
    compare_lt(card1, card2)
    card2 = Card("H", "Q")
    compare_lt(card1, card2)
    card2 = Card("H", "K")
    compare_lt(card1, card2)
    card2 = Card("H", "A")
    compare_lt(card1, card2)
    card1 = Card("C", "Q")
    card2 = Card("H", "Q")
    compare_lt(card1, card2)
    card2 = Card("H", "K")
    compare_lt(card1, card2)
    card2 = Card("H", "A")
    compare_lt(card1, card2)
    card1 = Card("C", "K")
    card2 = Card("H", "K")
    compare_lt(card1, card2)
    card2 = Card("H", "A")
    compare_lt(card1, card2)
    card1 = Card("C", "A")
    card2 = Card("H", "A")
    compare_lt(card1, card2)


def test_le():
    print("-" * 10 + "\nLess Than or Equal To\n" + "-" * 10)
    card1 = Card("C", 2)
    card2 = Card("H", 2)
    compare_le(card1, card2)
    card2 = Card("H", 3)
    compare_le(card1, card2)
    card1 = Card("C", 4)
    compare_le(card1, card2)


def test_eq():
    print("-" * 10 + "\nEqual To\n" + "-" * 10)
    card1 = Card("C", 2)
    card2 = Card("H", 2)
    compare_eq(card1, card2)
    card2 = Card("H", 3)
    compare_eq(card1, card2)


def test_ne():
    print("-" * 10 + "\nNot Equal To\n" + "-" * 10)
    card1 = Card("C", 2)
    card2 = Card("H", 2)
    compare_ne(card1, card2)
    card2 = Card("H", 3)
    compare_ne(card1, card2)


def test_gt():
    print("-" * 10 + "\nGreater Than\n" + "-" * 10)
    card1 = Card("C", 3)
    card2 = Card("H", 3)
    compare_gt(card1, card2)
    card2 = Card("H", 2)
    compare_gt(card1, card2)
    card1 = Card("C", "J")
    compare_gt(card1, card2)
    card2 = Card("H", "J")
    compare_gt(card1, card2)
    card1 = Card("C", "Q")
    compare_gt(card1, card2)
    card1 = Card("C", "K")
    compare_gt(card1, card2)
    card1 = Card("C", "A")
    compare_gt(card1, card2)
    card1 = Card("C", "Q")
    card2 = Card("H", "Q")
    compare_gt(card1, card2)
    card1 = Card("C", "K")
    compare_gt(card1, card2)
    card1 = Card("C", "A")
    compare_gt(card1, card2)
    card1 = Card("C", "K")
    card2 = Card("H", "K")
    compare_gt(card1, card2)
    card1 = Card("C", "A")
    compare_gt(card1, card2)
    card2 = Card("H", "A")
    compare_gt(card1, card2)


def test_ge():
    print("-" * 10 + "\nGreater Than or Equal To\n" + "-" * 10)
    card1 = Card("C", 3)
    card2 = Card("H", 3)
    compare_ge(card1, card2)
    card2 = Card("H", 2)
    compare_ge(card1, card2)
    card2 = Card("H", "J")
    compare_ge(card1, card2)


if __name__ == "__main__":
    test_lt()
    test_le()
    test_eq()
    test_ne()
    test_gt()
    test_ge()
