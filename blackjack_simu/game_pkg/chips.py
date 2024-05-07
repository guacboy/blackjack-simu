from tkinter import *
from PIL import Image, ImageTk

from display_pkg.style import *
from display_pkg.delete import Delete
from display_pkg.display import displays

# used to reset the balance and bet amount displays
# if user decides to reset the bet amount
bet_amount_total = []

# used to redo previous bet
saved_chip_color = []

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
        # creates a container for the poker chips
        self.poker_chip_container = Frame(self.root)
        self.poker_chip_container.place(anchor = CENTER,
                                        relx = 0.5,
                                        rely = 0.75)
        
        # opens and resizes the image
        self.resize_card = Image.open(f"assets/chips_png/{color}") \
                                .resize(CHIP_SIZE)
        self.resize_chip_label = ImageTk.PhotoImage(self.resize_card)
        
        # displays the poker chip
        self.poker_chip_label = Label(self.poker_chip_container,
                                      image = self.resize_chip_label,
                                      bg = BACKGROUND_COLOR)
        self.poker_chip_label.pack(side = LEFT)
        
        # adds the corresponding bet depending on the chip clicked
        self.bet_amount = Chips.add_bet(color,
                                        self.bet_amount,
                                        self.balance)
        self.balance = self.bet_amount[-1]
        self.bet_amount = self.bet_amount[0]
        
        # updates balance and bet labels
        Chips.update_score(self)
        
        return self.bet_amount, self.balance
    
    def add_bet(color,
                bet_amount,
                balance):
        # adds corresponding bet amount depending on the chip clicked
        if color == "black_chip.png":
            temp_bet_amount = 500
        elif color == "blue_chip.png":
            temp_bet_amount = 250
        elif color == "green(red)_chip.png":
            temp_bet_amount = 100
        elif color == "red(green)_chip.png":
            temp_bet_amount = 50
        elif color == "white_chip.png":
            temp_bet_amount = 25
        
        # checks if bet amount is less than or equal
        # to current balance
        if (temp_bet_amount <= balance):
            # appends to a list to be later sum up
            # for redo
            bet_amount_total.append(temp_bet_amount)
            saved_chip_color.append(color) #FIXME
            
            bet_amount += temp_bet_amount
            balance -= temp_bet_amount
        else:
            print("Insufficient funds.")
        return bet_amount, balance
    
    '''
    resets the bet amount
    '''
    def reset_bet(self):
        # redo's the balance and bet amount
        self.bet_amount -= sum(bet_amount_total)
        self.balance += sum(bet_amount_total)
        
        # avoids duplicates
        bet_amount_total.clear()
        
        try:
            # deletes poker chips display
            Delete.delete_all_poker_chips(self)
        except AttributeError:
            pass
        
        # updates balance and bet labels
        Chips.update_score(self)
    
    '''
    repeats the previous bet amount
    '''
    def redo_bet(self):
        try:
            print("Previous bet:", saved_chip_color)
            # displays previous poker chips and
            # repeats previous bet amount
            for i in range(len(saved_chip_color)):
                Chips.display_poker_chip(self,
                                         color = saved_chip_color[i])
            
            # updates balance and bet labels
            Chips.update_score(self)
        except IndexError:
            print("No previous bet.")

    '''
    confirms the bet amount
    '''
    def confirm_bet(self):
        # deletes bet request display
        Delete.delete_bet_request(self)
        
        try:
            if self.bet_amount > 0:
                # moves betting chips to the center of the table
                self.poker_chip_container.place(anchor = CENTER,
                                                relx = 0.5,
                                                rely = 0.45)
                pass
        except AttributeError:
            pass
        
        # updates balance and bet labels
        Chips.update_score(self)
        
        #updates the inital player's options
        Chips.update_init_game(self)
    
    '''
    updates the inital player's options
    '''
    def update_init_game(self):
        # checks if bet amount is a non-zero after update
        if self.bet_amount > 0:
            self.deal_button.pack(side = LEFT,
                                  padx = 10)
        else:
            self.deal_button.pack_forget()
            
    '''
    displays the balance and bet amount
    '''
    def display_score(self):
        # iterates through the labels to be displayed
        for display in displays["score"]:
            self.label = Label(self.root,
                               font = BALANCE_AND_BET_FONT,
                               bg = BACKGROUND_COLOR)
            
            # displays the current balance
            if display == "balance_label":
                self.balance_label = self.label
                self.balance_label.config(text = f"Balance\n${self.balance}")
            # displays the current bet amount
            elif display == "bet_amount_label":
                self.bet_amount_label = self.label
                self.bet_amount_label.config(text = f"Bet\n${self.bet_amount}")
                
        self.balance_label.place(anchor = CENTER,
                                 relx = 0.07,
                                 rely = 0.93)
        self.bet_amount_label.place(anchor = CENTER,
                                    relx = 0.19,
                                    rely = 0.93)
    
    '''
    updates balance and bet labels
    '''
    def update_score(self):
        #deletes the balance and bet labels
        Delete.delete_score(self)
        
        # displays the balance and bet amount
        Chips.display_score(self)