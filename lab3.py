#Lab 3 
#Maria Garic
import random

class Card:
    def __init__(self, suit, value): #constructor initizaliser. 
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value
        
    def getValue(self): 
        return self._value
    
    def getSuit(self):
        return self._suit
    
    def __str__(self): #Make sures that each card has a value and suit.
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        suit = ("hearts", "clubs", "diamonds", "spades")
        return f"{values[self._value - 1]} of {suit[self._suit - 1]}" #-1, corresponding value
 
class CardDeck:
    
    def __init__(self):
        self._cards = [Card(suit, value) for suit in range(1, 5) for value in range(1, 14)] #add new card object has value and suit.

    def shuffle(self):
        random.shuffle(self._cards)
        
    def getCard(self):
        return self._cards.pop() #remove + return 

    def size(self):
        return len(self._cards) # retuns size of cards remaning, by calculcating the lenght of the cards list[].
    
    def reset(self):
        self.__init__()

#Testing code 
deck = CardDeck()
deck.shuffle()
while deck.size()>0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))

