class Delete:
    '''
    deletes the main menu display
    '''    
    def delete_main_menu(self):
        self.main_menu_container.pack_forget()
        self.copyright_display.pack_forget()
    
    '''
    deletes initial player options display
    '''    
    def delete_init_game(self):
        self.init_options_container.pack_forget()
    
    '''
    deletes bet request display
    '''    
    def delete_bet_request(self):
        self.bet_request_container.place_forget()
        self.confirm_button.place_forget()
            
    '''
    deletes poker chips display
    '''
    def delete_all_poker_chips(self):
        self.poker_chip_container.place_forget()
    def delete_add_poker_chips(self):
        self.add_poker_chip_display.pack_forget()
        
    '''
    deletes game display
    '''
    def delete_game(self):
        self.card_options_container.pack_forget()
        
    '''
    deletes the blank card covering the dealer's second card
    '''    
    def delete_blank_card(self,
                          displayed_blank_cards):
        for card in displayed_blank_cards:
            card.place_forget()
    
    '''
    deletes any current cards in play
    '''    
    def delete_cards(self,
                     displayed_cards):
        for card in displayed_cards:
            card.place_forget()
            
    '''
    deletes the card totals display
    '''
    def delete_card_totals(self,
                           displayed_total_label):
        for label in displayed_total_label:
            label.place_forget()
            # self.dealer_total_display.place_forget()
            
    '''
    deletes the balance and bet labels
    '''
    def delete_balance_and_bet_amount(self):
        self.balance_display.place_forget()
        self.bet_amount_display.place_forget()
            
    '''
    deletes pause menu options
    '''
    def delete_pause_menu(self):
        self.pause_menu_options.pack_forget()
        
    '''
    deletes outcome display
    '''    
    def delete_check(self):
        self.check_display.pack_forget()