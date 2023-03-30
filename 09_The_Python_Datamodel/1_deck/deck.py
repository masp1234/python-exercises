class Deck:
    def __init__(self):
        self.cards = [2, 3, 4, 'K']

    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return f'{self.cards}'

    def __repr__(self):
        return f'{self.__dict__}'
    
    def __getitem__(self, key):
        return self.cards[key]
    
    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]

    def __add__(self, other):
        deck = Deck()
        deck.cards = self.cards + other.cards
        return deck
    

deck = Deck()
print(deck)
print(repr(deck))
