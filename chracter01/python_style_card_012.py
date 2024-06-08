import collections
from time import time
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    
    def __getitem__(self, position: int) -> Card:
        return self._cards[position]
    
    def __len__(self):
        return len(self._cards)
    
    def __contains__(self, card):
        print("+++++++++++++++++++++++")
        return card in self._cards

if __name__ == "__main__":
    frenchDeck = FrenchDeck()
    print(f"frenchDeck len: {len(frenchDeck)}")
    print(f"frenchDeck at index 0: {frenchDeck[0]}")
    print(f"frenchDeck at index -1: {frenchDeck[-1]}")

    loop = 0
    for ele in frenchDeck:
        print(f"index at {loop}: {frenchDeck[loop]}")
        loop += 1
        
    loop = 51
    for ele in reversed(frenchDeck):
        print(f"index at {loop}: {frenchDeck[loop]}")
        loop -= 1
    
    loop = 5
    for ele in range(loop):
        print(f"choice at {loop}: {choice(frenchDeck)}")
        loop -= 1
    
    
    start = time()
    print(f"Card(rank='2', suit='spades') in frenchDeck?: {Card('2', 'spades') in frenchDeck}")
    print(f"cost :{time() - start}")