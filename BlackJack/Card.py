"""Card

Attributes:
    suit (string): Holds the suit of the card (H, D, C, S)
    rank (string): Holds the rank of the card (A, 2-10, J, Q, K)

ToDo:

"""

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return str(self.rank) + str(self.suit[0]) 