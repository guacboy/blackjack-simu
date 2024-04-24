import random

class Deal():
    '''
    shuffles the cards in the deck
    '''    
    @staticmethod
    def shuffle_cards(total_cards):
        random.shuffle(total_cards)
    
    '''
    deals initial cards to player and dealer
    '''    
    @staticmethod
    def deal_cards(total_cards,
                   player_cards,
                   dealer_cards):
        for card in range(2):
            player_cards.append(total_cards.pop())
            dealer_cards.append(total_cards.pop())
        print("Player's cards:", player_cards)
        print("Dealer's cards:", dealer_cards)