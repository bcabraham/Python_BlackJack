"""Player

Attributes:
    hand (List of Cards) - Tracks player's hand in the current game
    name (string) - holds player's name
    bank (decimal) - tracks player's current money total
    is_dealer (bool)
ToDo:
    - Implement bet Method
    - Implement cleanupHand
"""

import Card

class Player:

    def __init__(self, name, bank, is_dealer):
        self.hand = []
        self.name = name
        self.bank = bank
        self.is_dealer = is_dealer
    
    def hit(self, card):
        self.hand.append(card)
    
    def stay(self):
        pass
    
    def split(self):
        pass
    
    def bet(self, amount):
        pass

    def cleanup_hand(self):
        pass

    def busted(self):
        pass
    
    def blackjack(self):
        pass