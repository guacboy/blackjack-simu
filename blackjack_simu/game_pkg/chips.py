from tkinter import *
from PIL import Image, ImageTk

from display_pkg.style import *
from display_pkg.delete import Delete

class Chips:
    def __init__(self,
                 bet_amount = 0,
                 balance = 1000):
        # total balance and bet amount
        self.bet_amount = bet_amount
        self.balance = balance
    
    '''
    displays current poker chips
    '''
    def display_poker_chip(self,
                           color):
        # opens and resizes the image
        self.resize_card = Image.open(f"assets/chips_png/{color}") \
                                .resize(CHIP_SIZE)
        self.resize_chip_display = ImageTk.PhotoImage(self.resize_card)
        
        # creates a container for the poker chips
        self.poker_chip_container = Frame(self.root)
        self.poker_chip_container.place(anchor = CENTER,
                                        relx = 0.5,
                                        rely = 0.75)
        
        # displays the poker chips
        self.poker_chip_display = Label(self.poker_chip_container,
                                        image = self.resize_chip_display,
                                        bg = BACKGROUND_COLOR)
        self.poker_chip_display.pack(side = LEFT)
        
        # adds the corresponding bet depending on the chip clicked
        self.bet_amount = Bet.add_bet(color,
                                      self.bet_amount,
                                      self.balance)
        self.balance = self.bet_amount[-1]
        self.bet_amount = self.bet_amount[0]
        
        # updates balance and bet labels
        Chips.update_balance_and_bet_amount(self)
        
        return self.bet_amount, self.balance
    
    '''
    resets the bet amount
    '''
    def reset_bet(self):
        try:
            # deletes poker chips display
            Delete.delete_all_poker_chips(self)
        except AttributeError:
            pass
    
    '''
    repeats the previous bet amount
    '''
    def redo_bet(self):
        pass

    '''
    confirms the bet amount
    '''
    def confirm_bet(self):
        # deletes bet request display
        Delete.delete_bet_request(self)
        
        try:
            # moves betting chips to the center of the table
            self.poker_chip_container.place(anchor = CENTER,
                                            relx = 0.5,
                                            rely = 0.45)
        except AttributeError:
            pass
        
        #updates the inital player's options
        Chips.update_init_game(self,
                               self.bet_amount)
    
    '''
    updates the inital player's options
    '''
    def update_init_game(self,
                         bet_amount):
        # checks if bet amount is a non-zero after update
        if bet_amount > 0:
            self.deal_button.pack(side = LEFT,
                                  padx = 10)
            
    '''
    displays the balance and bet amount
    '''
    def display_balance_and_bet_amount(self):
        # balance and bet amount labels
        balance_and_bet_amount_labels = [
            "balance",
            "bet_amount"
        ]
        
        # iterates through the labels to be displayed
        for label in balance_and_bet_amount_labels:
            self.label = Label(self.root,
                               font = BALANCE_AND_BET_FONT,
                               bg = BACKGROUND_COLOR)
            
            # displays the current balance
            if label == "balance":
                self.balance_display = self.label
                self.balance_display.config(text = f"Balance\n${self.balance}")
            # displays the current bet amount
            elif label == "bet_amount":
                self.bet_amount_display = self.label
                self.bet_amount_display.config(text = f"Bet\n${self.bet_amount}")
                
        self.balance_display.place(anchor = CENTER,
                                   relx = 0.07,
                                   rely = 0.93)
        self.bet_amount_display.place(anchor = CENTER,
                                      relx = 0.19,
                                      rely = 0.93)
    
    '''
    updates balance and bet labels
    '''
    def update_balance_and_bet_amount(self):
        #deletes the balance and bet labels
        Delete.delete_balance_and_bet_amount(self)
        
        # displays the balance and bet amount
        Chips.display_balance_and_bet_amount(self)
        
class Bet:
    @staticmethod
    def add_bet(color,
                bet_amount,
                balance):
        if (bet_amount <= balance):
            # adds corresponding bet amount depending on the chip clicked
            if color == "black_chip.png":
                bet_amount += 500
                balance -= 500
            elif color == "blue_chip.png":
                bet_amount += 250
                balance -= 250
            elif color == "green(red)_chip.png":
                bet_amount += 100
                balance -= 100
            elif color == "red(green)_chip.png":
                bet_amount += 50
                balance -= 50
            elif color == "white_chip.png":
                bet_amount += 25
                balance -= 25
        else:
            print("Insufficient funds.")
        return bet_amount, balance