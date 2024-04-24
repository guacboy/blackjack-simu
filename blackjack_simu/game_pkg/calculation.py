from tkinter import *

from style import *
from game_pkg.conversion import Conversion

class Calculation:
    '''
    calls the conversion class to assign png files with metadata values
    then, calculates the total to pass into the check method
    '''
    def sum_of_curr_cards(self,
                          player_cards,
                          dealer_cards):
        # assigns png files with metadata values and
        # adds the metadata values into a total amount for
        # the player and dealer
        self.player_total = Conversion.convert_png_to_values(self,
                                                             player_cards)
        self.dealer_total = Conversion.convert_png_to_values(self,
                                                             dealer_cards)
        
        return self.player_total, self.dealer_total
    
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