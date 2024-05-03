from tkinter import *
from tkinter import ttk
from os import listdir

import os
import sys

from game_pkg.deck import Deck
from game_pkg.chips import Chips
from display_pkg.style import *
from display_pkg.delete import Delete
from display_pkg.display import Display, displays

# cards used during play
total_cards = [
    # iterates through the folder containing the cards
    # and moves them into a list
    image for image in os.listdir("assets/cards_png")
    if (image.endswith(".png"))
] * 6

# cards that are dealt to the player and dealer
player_cards = []
dealer_cards = []

# cards stored to be later deleted after round resets
displayed_cards = []
displayed_blank_cards = []
# labels stored to be later deleted after round resets
displayed_total_label = []

# notifies when the program is closed
CLOSE_PROGRAM = "Program is closing.."
        
class MainMenu():   
    root = Tk()
    root.wm_attributes("-fullscreen", "True")
    root.config(background = BACKGROUND_COLOR)
    
    def __init__(self):
        # initializes the bet and balance variables
        self.bet_amount = 0
        self.balance = 1000
        self.chips = Chips(bet_amount = self.bet_amount,
                           balance = self.balance)
    
    '''
    displays the main menu options:
    new game, practice mode, and exit game
    '''   
    def display_main_menu(self):
        # notifies when the program is opened
        print("Program is running..")
        
        # creates a container for the main menu,
        # except the copyright label
        self.main_menu_container = Frame(self.root,
                                         bg = BACKGROUND_COLOR)
        self.main_menu_container.pack(anchor = CENTER)
        
        # iterates through the dictionary to be displayed
        for display in displays["main_menu"]:
            root = self.main_menu_container
            
            if display == "copyright_label":
                root = self.root
            
            self.label = Label(root,
                               fg = TEXT_COLOR,
                               bg = BACKGROUND_COLOR)
            
            # displays the game title
            if display == "title_label":
                self.title_label = self.label
                self.title_label.config(text = "Blackjack v0.0.3",
                                          font = TITLE_FONT)
            # displays the trademark title
            elif display == "copyright_label":
                self.copyright_label = self.label
                self.copyright_label.config(text = "© Dylan Nguyen 2024",
                                              font = COPYRIGHT_FONT)
                
        self.title_label.pack(anchor = CENTER,
                                pady = 100)
        self.copyright_label.pack(side = BOTTOM)
        
        # creates a container for the option buttons
        self.main_menu_options_container = Frame(self.main_menu_container,
                                                 bg = BACKGROUND_COLOR)
        self.main_menu_options_container.pack(anchor = CENTER)
        
        # iterates through the dictionary to be displayed
        for display in displays["main_menu"]:
            self.button = Button(self.main_menu_options_container,
                                     font = MAIN_MENU_FONT,
                                     relief = FLAT)
            
            # displays the new game button
            if display == "new_game_button":
                self.new_game_button = self.button
                self.new_game_button.config(text = "New Game",
                                            # deletes main menu and starts up
                                            # a new game
                                            command = lambda: self.init_new_game())
            # displays the practice button
            elif display == "practice_button":
                self.practice_button = self.button
                self.practice_button.config(text = "Practice")
            # displays the exit button
            elif display == "exit_button":
                self.exit_button = self.button
                self.exit_button.config(text = "Exit",
                                        # closes the program
                                        command = lambda: sys.exit(CLOSE_PROGRAM))
        
        self.new_game_button.pack()
        self.practice_button.pack(fill = "x",
                                  pady = 25)
        self.exit_button.pack(fill = "x")
    
    '''
    clicking the new game button will delete
    the main menu options and
    loads a new game
    '''    
    def init_new_game(self):
        # deletes the main menu display
        Delete.delete_main_menu(self)
        
        # shuffles cards in the deck
        Deck.shuffle_cards(total_cards)
        
        # displays game board with initial player's options
        Blackjack.display_init_game(self)
        
        # updates balance and bet labels
        Chips.display_score(self)
        
        # displays the menu option button
        Blackjack.display_menu_option(self)

class Blackjack(MainMenu):
    '''
    resets the game for the next round
    '''    
    def reset_round(self):
        try:
            # deletes any current cards in play
            Delete.delete_cards(self,
                                displayed_cards)
            
            # deletes the card totals display
            Delete.delete_card_totals(self,
                                      displayed_total_label)
            
            # deletes any addtional poker chips winnings
            Delete.delete_add_poker_chips(self)
            
            # deletes outcome display
            Delete.delete_check(self)
        except AttributeError:
            pass
        
        # resets all the stats
        player_cards.clear()
        dealer_cards.clear()
        self.player_total = 0
        self.dealer_total = 0
    
    '''
    displays game board with initial player's options
    '''    
    def display_init_game(self):
        try:
            # deletes inital player options
            Delete.delete_init_game(self)
            
            # deletes game display
            Delete.delete_game(self)
            
            # deletes the blank card covering the dealer's second card
            Delete.delete_blank_card(self,
                                     displayed_blank_cards)
            
            # updates balance and bet labels
            Chips.update_score(self)
        except AttributeError:
            pass
        
        # creates a container for the player's options
        self.init_options_container = Frame(self.root,
                                            bg = BACKGROUND_COLOR)
        self.init_options_container.pack(side = BOTTOM,
                                         pady = 25)
        
        # iterates through the dictionary to be displayed
        for display in displays["init_game"]:
            self.button = Button(self.init_options_container,
                                 compound = CENTER,
                                 activebackground = BACKGROUND_COLOR,
                                 highlightthickness = 0,
                                 bd = 0)
            
            if display == "bet_button":
                image = "choices_png/bet_button.png"
                variable = "resize_bet_button"
            elif display == "deal_button":
                image = "choices_png/deal_button.png"
                variable = "resize_deal_button"
            
            # resizes the image    
            Display.resize_image(self,
                                 image = image,
                                 resize = PLAYER_OPTIONS_SIZE,
                                 variable = variable)
            
            # displays the bet button
            if display == "bet_button":
                self.bet_button = self.button
                self.bet_button.config(image = self.resize_bet_button,
                                       # displays the bet request prompt
                                       command = lambda: Blackjack.display_bet_request(self))
            # displays the deal button    
            elif display == "deal_button":
                self.deal_button = self.button
                self.deal_button.config(image = self.resize_deal_button,
                                       # starts the turn
                                       command = lambda: Blackjack.display_game(self))
                
        self.bet_button.pack(side = LEFT,
                             padx = 10)
        
        try:
            # checks if bet amount is a non-zero
            if self.bet_amount > 0:
                self.deal_button.pack(side = LEFT,
                                    padx = 10)
        except AttributeError:
            pass  
        
    '''
    displays the bet request prompt
    '''    
    def display_bet_request(self):
        # resets the game for the next round
        Blackjack.reset_round(self)
        
        # resets the bet amount
        self.bet_amount = 0
        
        # creates a container for the bet requests
        self.bet_request_container = Frame(self.root,
                                           bg = BACKGROUND_COLOR)
        self.bet_request_container.place(anchor = CENTER,
                                         relx = 0.5,
                                         rely = 0.4)
        
        # displays the bet request prompt
        self.bet_request_label = Label(self.bet_request_container,
                                       text = "PLACE YOUR BETS",
                                       font = BET_REQUEST_FONT,
                                       bg = BACKGROUND_COLOR)
        self.bet_request_label.pack(side = TOP,
                                    padx = 25,
                                    pady = 25)
        
        # iterates through the dictionary to be displayed
        for display in displays["bet_request"]:
            root = self.bet_request_container
            
            if display == "reset_button":
                image = "betreq_png/reset_button.png"
                variable = "resize_reset_button"
            elif display == "redo_button":
                image = "betreq_png/redo_button.png"
                variable = "resize_redo_button"
            elif display == "confirm_button":
                root = self.root
                image = "betreq_png/confirm_button.png"
                variable = "resize_confirm_button"
                
            self.button = Button(root,
                                 compound = CENTER,
                                 activebackground = BACKGROUND_COLOR,
                                 highlightthickness = 0,
                                 bd = 0)
            
            # resizes the image
            Display.resize_image(self,
                                 image = image,
                                 resize = PLAYER_OPTIONS_SIZE,
                                 variable = variable)
        
            # displays the reset button
            if display == "reset_button":
                self.reset_button = self.button
                self.reset_button.config(image = self.resize_reset_button,
                                         command = lambda: Chips.reset_bet(self))
            # displays the redo button
            elif display == "redo_button":
                self.redo_button = self.button
                self.redo_button.config(image = self.resize_redo_button)
            # displays the confirm button
            elif display == "confirm_button":
                self.confirm_button = self.button
                self.confirm_button.config(image = self.resize_confirm_button,
                                           # confirms bet and
                                           # closes bet request menu
                                           command = lambda: Chips.confirm_bet(self))
          
        self.reset_button.pack(side = LEFT,
                               padx = (0, 15))
        
        # poker chips for when selecting a bet amount
        poker_chips = [
            # iterates through the folder containing the poker chips
            # and moves them into a list
            image for image in os.listdir("assets/chips_png")
            if (image.endswith(".png"))
        ]

        # iterates through the poker chips to display their buttons
        for chip in poker_chips:
            # resizes the image
            Display.resize_image(self,
                                 image = f"chips_png/{chip}",
                                 resize = CHIP_SIZE_BUTTON,
                                 variable = "resize_chip_label")
            
            # displays the poker chips buttons
            self.bet_request_button = Button(self.bet_request_container,
                                            image = self.resize_chip_label,
                                            compound = CENTER,
                                            activebackground = BACKGROUND_COLOR,
                                            highlightthickness = 0,
                                            bd = 0)
            self.bet_request_button.pack(side = LEFT)
            # keeps a reference to prevent it from being destroyed
            self.bet_request_button.image = self.resize_chip_label
            
            if chip == "black_chip.png":
                self.bet_request_button.config(command = lambda: Chips.display_poker_chip(self,
                color = "black_chip.png"))
            elif chip == "blue_chip.png":
                self.bet_request_button.config(command = lambda: Chips.display_poker_chip(self,
                color = "blue_chip.png"))
            elif chip == "green(red)_chip.png":
                self.bet_request_button.config(command = lambda: Chips.display_poker_chip(self,
                color = "green(red)_chip.png"))
            elif chip == "red(green)_chip.png":
                self.bet_request_button.config(command = lambda: Chips.display_poker_chip(self,
                color = "red(green)_chip.png"))
            elif chip == "white_chip.png":
                self.bet_request_button.config(command = lambda: Chips.display_poker_chip(self,
                color = "white_chip.png"))
        
        self.redo_button.pack(side = LEFT,
                              padx = (15, 0))
        self.confirm_button.place(relx = 0.446,
                                  rely = 0.57)

    
    '''
    displays the menu option button
    '''        
    def display_menu_option(self):    
        # allows player to pause game
        # and display the in-game menu options
        self.menu_option_button = Button(self.root,
                                         text = "⚙",
                                         font = ("Arial", 30),
                                         relief = FLAT,
                                         # opens the pause menu
                                         command = lambda: Blackjack.display_pause_menu_option(self))
        self.menu_option_button.pack(anchor = NE,
                                     padx = 25,
                                     pady = 25)
        
    '''
    displays game board with player's options
    '''
    def display_game(self):
        # deletes inital player options
        Delete.delete_init_game(self)
        
        # resets the game for the next round
        Blackjack.reset_round(self)
        
        # deals cards to player and dealer
        Deck.deal_cards(total_cards,
                        player_cards,
                        dealer_cards)
        
        # creates a container for the player's options
        self.card_options_container = Frame(self.root,
                                            bg = BACKGROUND_COLOR)
        self.card_options_container.pack(side = BOTTOM,
                                         pady = 25)
        
        # iterates through the dictionary to be displayed
        for display in displays["game"]:
            self.button = Button(self.card_options_container,
                                 compound = CENTER,
                                 activebackground = BACKGROUND_COLOR,
                                 highlightthickness = 0,
                                 bd = 0)
            
            if display == "double_button":
                image = "choices_png/double_button.png"
                variable = "resize_double_button"
            elif display == "hit_button":
                image = "choices_png/hit_button.png"
                variable = "resize_hit_button"
            elif display == "stand_button":
                image = "choices_png/stand_button.png"
                variable = "resize_stand_button"
            elif display == "split_button":
                image = "choices_png/split_button.png"
                variable = "resize_split_button"
                
            # resizes the image
            Display.resize_image(self,
                                 image = image,
                                 resize = PLAYER_OPTIONS_SIZE,
                                 variable = variable)
            
            # displays the double button
            if display == "double_button":
                self.double_button = self.button
                self.double_button.config(image = self.resize_double_button,
                                          # adds another bet and card,
                                          # then ends turn
                                          command = lambda: Choice.double(self))
            # displays the hit button
            elif display == "hit_button":
                self.hit_button = self.button
                self.hit_button.config(image = self.resize_hit_button,
                                       # adds another card
                                       command = lambda: Choice.hit(self,
                                                                    total_cards,
                                                                    player_cards))
            # displays the stand button
            elif display == "stand_button":
                self.stand_button = self.button
                self.stand_button.config(image = self.resize_stand_button,
                                         # ends turn
                                         command = lambda: Choice.stand(self))
            # displays the split button
            elif display == "split_button":
                self.split_button = self.button
                self.split_button.config(image = self.resize_split_button,
                                         # adds another bet
                                         # and splits the cards evenly
                                         command = lambda: print("Split"))
        
        # checks if current cards meet the requirements
        # to double down;
        # if player has a 9, 10, or 11 without an ace, or
        # if player has a 16, 17, or 18 with an ace
        if ((self.player_total >= 9 and
            self.player_total <= 11 and
            player_cards[0].startswith("ace") != False or
            player_cards[1].startswith("ace") != False) or
            self.player_total >= 16 and
            self.player_total <= 18 and
            player_cards[0].startswith("ace") or
            player_cards[1].startswith("ace")):
                self.double_button.pack(side = LEFT,
                                        padx = 10)  
                               
        self.hit_button.pack(side = LEFT,
                             padx = 10)
        self.stand_button.pack(side = LEFT,
                               padx = 10)
        
        # iterates through player's cards to check if the cards
        # meet the requirements to split;
        # if player has two of the same value cards
        for card in player_cards:
            # returns a stop index to avoid comparing the
            # card types
            stop_idx = card.find("_")
            first_card = player_cards[0]
            second_card = player_cards[1]
            
            # compares the name of the png files
            # excluding the card type
            if first_card[:stop_idx] == second_card[:stop_idx]:
                self.split_button.pack(side = LEFT,
                                       padx = 10)
        
        # displays current cards in play and
        # adds the sum of cards
        Blackjack.update_cards(self)
    
    '''
    displays current cards in play
    '''    
    def display_cards(self):
        # x-coords for where the cards are placed
        player_card_placement_x = dealer_card_placement_x = 875
        
        # loops to display current cards in play
        for index, card in enumerate(player_cards + dealer_cards):
            try:                          
                # resizes the image
                Display.resize_image(self,
                                     image = f"cards_png/{card}",
                                     resize = CARD_SIZE,
                                     variable = "resize_card_label")
                
                self.label = Label(self.root)
                
                # limits to only viewing the player's cards,
                # displaying the player's current cards in play
                if index < len(player_cards):
                    self.player_cards_label = self.label
                    self.player_cards_label.config(image = self.resize_card_label)
                    
                    self.player_cards_label.place(x = player_card_placement_x,
                                                  y = 700)
                    
                    # keeps a reference to prevent it from being destroyed
                    self.player_cards_label.image = self.resize_card_label
                    
                    # appends to the displayed cards list
                    # to be later deleted when round resets
                    displayed_cards.append(self.player_cards_label)
                    
                    # moves next card to the right of previous card 
                    player_card_placement_x += 25
                    
                # limits to only viewing the dealer's cards,
                # displaying dealer's current cards in play
                else: 
                    self.dealer_cards_label = self.label
                    self.dealer_cards_label.config(image = self.resize_card_label)
                    
                    self.dealer_cards_label.place(x = dealer_card_placement_x,
                                                  y = 50)
                    
                    # keeps a reference to prevent it from being destroyed
                    self.dealer_cards_label.image = self.resize_card_label 
                    
                    # appends to the displayed cards list
                    # to be later deleted when round resets
                    displayed_cards.append(self.dealer_cards_label)
                    
                    # covers the second card of the dealer's hand by
                    # displaying a blank card over it
                    
                    # moves next card to the right of previous card 
                    dealer_card_placement_x += 25       
            except IndexError:
                print("All cards are dealt.")
                
        # resizes the image
        Display.resize_image(self,
                             image = "blank_card.png",
                             resize = CARD_SIZE,
                             variable = "resize_blank_card_label")
        
        # displays a blank card over the second
        # dealer's card
        self.blank_cards_label = Label(self.root,
                                       image = self.resize_blank_card_label)
        self.blank_cards_label.place(x = 900,
                                     y = 50)
        
        # appends to the displayed blank cards list
        # to be later deleted when round resets
        displayed_blank_cards.append(self.blank_cards_label)
    
    '''
    updates current cards in play and
    the sum of cards
    '''        
    def update_cards(self): 
        # displays current cards in play
        Blackjack.display_cards(self)
        
        # calls the conversion class to assign png files with metadata values
        # then, calculates the total to pass into the check method
        self.player_total =  Deck.convert_png_to_values(self,
                                                        player_cards)
        self.dealer_total =  Deck.convert_png_to_values(self,
                                                        dealer_cards)
        
        print("Player's total:", self.player_total)
        print("Dealer's total:", self.dealer_total)
        
        Deck.display_card_totals(self,
                                 displayed_total_label)
        
        # passes in the total amounts and
        # checks for win conditions
        Check.auto_check(self,
                         player_cards,
                         self.player_total,
                         dealer_cards,
                         self.dealer_total)
        return self.player_total, self.dealer_total
            
    '''
    displays the menu options and pauses the game,
    allowing user to return to main menu or
    quit the program
    '''    
    def display_pause_menu_option(self):
        # creates a container for the pause menu options
        self.pause_menu_options = Frame(self.root)
        self.pause_menu_options.pack(anchor = CENTER,
                                     pady = 80)
        
        # displays the pause text
        self.pause_label = Label(self.pause_menu_options,
                                 text = "== PAUSE ==",
                                 font = PAUSE_TITLE_FONT)
        self.pause_label.pack(side = TOP,
                              pady = 25,
                              padx = 30)
        
        # iterates through the dictionary to be displayed
        for display in displays["pause_menu"]:
            self.button = Button(self.pause_menu_options,
                                 font = PAUSE_OPTION_FONT,
                                 relief = FLAT)
            
            # displays the main menu button
            if display == "main_menu_button":
                self.main_menu_button = self.button
                self.main_menu_button.config(text = "Main Menu",
                                             # returns to the main menu
                                             command = lambda: print("Main Menu"))
            # displays the main menu button
            elif display == "quit_button":
                self.quit_button = self.button
                self.quit_button.config(text = "Quit",
                                             # closes the program
                                             command = lambda: sys.exit(CLOSE_PROGRAM))
            # displays the main menu button
            elif display == "resume_button":
                self.resume_button = self.button
                self.resume_button.config(text = "Resume",
                                             # closes pause menu and resumes game
                                             command = lambda: Delete.delete_pause_menu(self))
        
        self.main_menu_button.pack(fill = "x")
        self.quit_button.pack(fill = "x")
        self.resume_button.pack(pady = 25,
                                fill = "x")
        
class Check(Blackjack):
    '''
    auto-checks for win conditions between player and dealer
    '''
    def auto_check(self,
                   player_cards,
                   player_total,
                   dealer_cards,
                   dealer_total):
        win = None
        
        # checks for similar conditions as below
        if (player_total == 21 and
            len(player_cards) == 2 or
            dealer_total == 21 and
            len(dealer_cards) == 2 or
            player_total > 21 or
            dealer_total > 21):
            # checks if player has blackjack
            # within the first two cards
            if (player_total == 21 and
                len(player_cards) == 2):
                # displays the player's blackjack text
                win = True
                print("Blackjack!")
        
            # checks if dealer has blackjack
            # within the first two cards
            elif (dealer_total == 21 and
                len(dealer_cards) == 2):
                # displays the dealer's blackjack text
                win = False
                print("Dealer wins!")
                
            # checks if player and dealer both have
            # blackjacks within the first two cards
            elif (player_total == 21 and
                len(player_cards) == 2 and
                dealer_total == 21 and
                len(dealer_cards) == 2):
                # displays the push text
                print("Push!")
            
            # checks if player has over 21 at any point
            elif player_total > 21:
                # displays the bust text
                win = False
                print("Bust!")
                
            # checks if dealer has over 21 at any point
            elif dealer_total > 21:
                # displays the bust text
                win = True
                print("Dealer bust!")

            # checks for player's win condition
            if win:
                # adds bet amount to money
                self.balance += self.bet_amount
                
                # displays the winning poker chips
                self.add_poker_chip_label = Label(self.poker_chip_container,
                                                  image = self.resize_chip_label,
                                                  bg = BACKGROUND_COLOR)
                self.add_poker_chip_label.pack(side = LEFT)
            elif win == False:
                # resets the bet amount
                self.bet_amount = 0
                
                # deletes the poker chips
                Delete.delete_all_poker_chips(self)
            elif win == None:
                pass
                
            # displays game board with initial player's options
            Blackjack.display_init_game(self)
    
    '''
    checks for win conditions between player and dealer
    after player ends turn
    '''        
    def manual_check(self,
                     player_total,
                     dealer_total):
        win = None
        
        try:
            # checks if player's total is higher than dealer's total
            if (player_total > dealer_total and
                player_total <= 21):
                # displays the player winning text
                win = True
                print("Player wins!")
            
            # checks if player's total is lower than dealer's total
            elif (player_total < dealer_total and
                dealer_total <= 21):
                # displays the dealer winning text
                win = False
                print("Dealer wins!")
            
            # checks if player's total is equal to dealer's total    
            elif (player_total == dealer_total and
                player_total <= 21 and
                dealer_total <= 21):
                # displays the push text
                print("Push!")
                
            # checks for player's win condition
            if win:
                # adds bet amount to money
                self.balance += self.bet_amount
                
                # displays the winning poker chips
                self.add_poker_chip_label = Label(self.poker_chip_container,
                                                  image = self.resize_chip_label,
                                                  bg = BACKGROUND_COLOR)
                self.add_poker_chip_label.pack(side = LEFT)
            elif win == False:
                # resets the bet amount
                self.bet_amount = 0
                
                # deletes the poker chips
                Delete.delete_all_poker_chips(self)
            elif win == None:
                pass
                
            # displays game board with initial player's options
            Blackjack.display_init_game(self)
        except AttributeError:
            pass
            
class Choice:
    '''
    adds another card
    '''
    def hit(self,
            total_cards,
            cards):
        cards.append(total_cards.pop())
        print("Added:", cards[-1])
        
        # updates current cards in play and
        # the sum of cards
        Blackjack.update_cards(self)

    '''
    ends turn and passes move to dealer
    '''
    def stand(self):
        Choice.dealer_move(self,
                           self.dealer_total)
        if self.dealer_total <= 21:
            # checks for win conditions between player and dealer
            # after player ends turn
            Check.manual_check(self,
                            self.player_total,
                            self.dealer_total)
    
    '''
    adds another card and another bet
    '''
    def double(self):
        Choice.hit(self,
                   total_cards,
                   player_cards)
        Choice.stand(self)
    
    '''
    splits card sets into two
    '''
    def split(self):
        print("Split")
    
    '''
    dealer continues to hit until their total is 17
    '''
    def dealer_move(self,
                    dealer_total):
        while dealer_total < 17:
            Choice.hit(self,
                       total_cards,
                       dealer_cards)
            dealer_total = Deck.convert_png_to_values(self,
                                                      dealer_cards)
        
if __name__ == "__main__":
    MainMenu().display_main_menu()
    root = mainloop()
    print(CLOSE_PROGRAM)