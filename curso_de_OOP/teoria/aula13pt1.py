# Herança

""" A herança é a capacidade de definir uma nova classe que seja
uma versão modificada de uma classe já existente.
"""


import random


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2) -> None:
        self.suit = suit
        self.rank = rank

    # Exibindo objetos card de modo que as pessoas possam ler mais facilmente

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self) -> str:
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # conferir os naipes
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False

        # os naipes são os mesmos... conferir valores
        return self.rank < other.rank


# Verificando
queen_of_diamonds = Card(1, 12)
print(queen_of_diamonds)


# __lt__ representa "menos que"
"""recebe dois parâmetros, self e other, e True
se self for estritamente menor que other.
"""

# Poderiamos escrever __lt__ de forma mais concisa usando tuplas
"""
def __lt__(self, other):
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return t1 < t2
"""

# Agora vamos definir o baralho (Deck)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


""" Esse join significa que para cada string em res, vamos adicionar um
'/n' entre elas, i.e., estamos quebrando a linha entre as cartas.
"""

# Queremos criar a classe "mão", que algumas mas não todas semelhanças com o Baralho


class Hand(Deck):
    """Represents a hand of playing cards."""

    # Escrevendo um __init__ para que Hand (filho) ignore o __init__ de Deck (pai)
    def __init__(self, label=''):
        self.cards = []
        self.label = label
