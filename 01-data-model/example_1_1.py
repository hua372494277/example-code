import collections

# collections模块的namedtuple子类不仅可以使用item的index访问item，还可以通过item的name进行访问。
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]



if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))

    from random import choice
    print(choice(deck))

    # print the top 3 cards
    print(deck[:3])
    # only print 'A' cards
    print(deck[12::13])

    # print all cards
    for card in deck:
        print(card)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]


    for card in sorted(deck, key=spades_high):
        print(card)