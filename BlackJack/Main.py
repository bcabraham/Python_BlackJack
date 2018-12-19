import Deck
import Card
import Player

numDecks = 1

deck = Deck.Deck(numDecks)
# print(deck)

deck.shuffle()
# print("shuffled deck:")
# print(deck)

dealer = Player.Player("Dealer", 1000.00, True)
player = Player.Player("Bryan", 500.00, False)

