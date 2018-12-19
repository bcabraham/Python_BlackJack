import Card



class Deck:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__ (self, numDecks):
        self.deck = []
        for x in range(0,numDecks):
            for suit in self.suits:
                for rank in self.ranks:
                    card = Card.Card(suit, rank)
                    self.deck.append(card)
        
        print(F"Created {numDecks} deck" + ("" if numDecks == 1 else "s"))

    def shuffle(self):
        pass

    def __str__(self):
        return ', '.join([str(c) for c in self.deck])

