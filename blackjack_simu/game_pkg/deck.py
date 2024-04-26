import random
from tkinter import *
from PIL import Image, PngImagePlugin

from display_pkg.style import *

class Deck:
    '''
    assigns png files with metadata values for calculations,
    passes in either player's cards or dealer's cards
    '''
    def convert_png_to_values(self,
                              cards):
        self.total_value = 0
        
        # checks if ace needs to equal to 1 or 11
        self.check_total = 0
        
        # iterates through the cards in play
        # and assigns the png files with metadata values
        for card in cards:
            if card.startswith("two"):
                self.card_value = "2"
                self.check_total += 2
            if card.startswith("three"):
                self.card_value = "3"
                self.check_total += 3
            if card.startswith("four"):
                self.card_value = "4"
                self.check_total += 4
            if card.startswith("five"):
                self.card_value = "5"
                self.check_total += 5
            if card.startswith("six"):
                self.card_value = "6"
                self.check_total += 6
            if card.startswith("seven"):
                self.card_value = "7"
                self.check_total += 7
            if card.startswith("eight"):
                self.card_value = "8"
                self.check_total += 8
            if card.startswith("nine"):
                self.card_value = "9"
                self.check_total += 9
            if (card.startswith("ten") or
                card.startswith("jack") or
                card.startswith("queen") or
                card.startswith("king")):
                self.card_value = "10"
                self.check_total += 10
            if card.startswith("ace"):
                self.check_total += 1
                if self.check_total <= 11:
                    self.card_value = "11"
                else:
                    self.card_value = "1"
                
            # opens image
            self.card_image = Image.open(f"assets/cards_png/{card}")
            
            # assigns the metadata to the card and saves info
            self.card_metadata = PngImagePlugin.PngInfo()
            self.card_metadata.add_text("value",
                                        self.card_value)
            self.card_image.save("value.png",
                                 pnginfo = self.card_metadata)
            
            # opens the image again and
            # gets the value of new image
            self.card_image = Image.open("value.png")
            value = self.card_image.info.get("value")
            
            # calculates the total value from their metadata
            self.total_value += int(value)       
        return self.total_value
    
    '''
    displays the card's total above the current cards in play
    '''
    def display_card_totals(self,
                            displayed_total_label):
        # displays the total values of player and dealer
        card_total_labels = [
            "player",
            "dealer"
        ]
        
        # iterates through the labels to display
        for label in card_total_labels:
            self.label = Label(self.root,
                               font = CARD_TOTAL_FONT,
                               bg = BACKGROUND_COLOR)
            
            # displays player's card total
            if label == "player":
                self.player_total_display = self.label
                self.player_total_display.config(text = f"({self.player_total})")
                # appends to the displayed total label list
                # to be later deleted when round resets
                displayed_total_label.append(self.player_total_display)
        
        self.player_total_display.place(anchor = CENTER,
                                        relx = 0.5,
                                        rely = 0.62)
    
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