from Card import Card


class Deck:
    def __init__(self):
        self.cards = Deck.fill_the_deck()

    @staticmethod
    def fill_the_deck():
        fresh_set_of_cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        for suit in suits:
            for rank in ranks:
                fresh_set_of_cards.append(Card(suit, rank))

        return fresh_set_of_cards


new_deck = Deck()

for card in new_deck.cards:
    print(card)

