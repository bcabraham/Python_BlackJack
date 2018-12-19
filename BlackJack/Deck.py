"""Deck

Attributes:
    deck (list of Cards)
    numDeck (int)


ToDo:
"""

import Card
import random

class Deck:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    """List of Suits"""
    ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    """List of Card Ranks"""
    
    def __init__ (self, numDecks):
        self.deck = []
        self.numDecks = numDecks
        self.insert_cards()
        print(F"Created {numDecks} deck" + ("" if numDecks == 1 else "s"))

    def insert_cards(self):
        for x in range(0,self.numDecks):
            for suit in self.suits:
                for rank in self.ranks:
                    card = Card.Card(suit, rank)
                    self.deck.append(card)

    def shuffle(self):
        """
        -- To shuffle an array a of n elements (indices 0..n-1):
        for i from n−1 downto 1 do
            j ← random integer such that 0 ≤ j ≤ i
            exchange a[j] and a[i]
        """
        for i in range(len(self.deck)-1, 0, -1):
            random.seed()
            j = random.randrange(0, i)
            card = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = card
        
    def deal(self):
        if len(self.deck) == 0:
            self.insert_cards()
            self.shuffle()
            print("Shuffling new deck")
        return self.deck.pop(0)

    def __str__(self):
        return ', '.join([str(c) for c in self.deck])

