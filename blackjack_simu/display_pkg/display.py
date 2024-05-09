from tkinter import *
from PIL import Image, ImageTk

# dictionary for buttons/labels
displays = {
    "curr_display": "",
    "main_menu": {
        "title_label": "title",
        "copyright_label": "copyright",
        "new_game_button": "new_game",
        "practice_button": "practice",
        "exit_button": "exit",
    },
    "init_game": {
        "bet_button": "bet",
        "deal_button": "deal" 
    },
    "bet_request": {
        "reset_button": "reset",
        "redo_button": "redo",
        "confirm_button": "confirm"
    },
    "game": {
        "double_button": "double",
        "hit_button": "hit",
        "stand_button": "stand",
        "split_button": "split"
    },
    "pause_menu": {
        "main_menu_button": "main_menu",
        "quit_button": "quit",
        "resume_button": "resume"
    },
    "card_total": {
        "player_label": "player",
        "dealer_label": "dealer"
    },
    "score": {
        "balance_label": "balance",
        "bet_amount_label": "bet_amount"
    }
}

class Display:
    '''
    passes in the image, resize value, and variable name,
    and resizes the image and assigns it to the given variable
    '''
    def resize_image(self,
                     image,
                     resize,
                     variable):
        # opens and resizes the image
        self.image = Image.open(f"assets/{image}") \
                            .resize(resize)
        self.resized_image = ImageTk.PhotoImage(self.image)
        
        # sets the variable attribute to the resized image value
        setattr(self,
                variable,
                self.resized_image)
        # returns the variable attribute
        return getattr(self, variable)