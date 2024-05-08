'''

'''

import os

'''
when testing out custom decks, remember:
1. disable shuffling (under init_new_game)
2. cards appear in descending order
3. first card is dealt to player, then dealer, and so forth
'''

# original deck
total_cards = [
    # iterates through the folder containing the cards
    # and moves them into a list
    image for image in os.listdir("assets/cards_png")
    if (image.endswith(".png"))
] * 6

# deck that gives player/dealer an immediate blackjack
blackjack_player = [
    "six_club.png",
    "jack_club.png",    # player blackjack
    "ace_diamond.png",
    "ace_club.png"
]

blackjack_dealer = [
    "jack_club.png"     # dealer blackjack
    "six_club.png",
    "ace_diamond.png",
    "ace_club.png"
]

# deck that allows the player to double down
double_cards_9 = [
    "eight_club.png",   # dealer stops at 17
    "jack_club.png",    # player double
    "three_diamond.png",
    "three_club.png",
    "six_diamond.png",
    "six_club.png"
]

double_cards_10 = [
    "eight_club.png",   # dealer stops at 17
    "jack_club.png",    # player double
    "three_diamond.png",
    "four_club.png",
    "six_diamond.png",
    "six_club.png"
]

double_cards_11 = [
    "eight_club.png",   # dealer stops at 17
    "jack_club.png",    # player double
    "three_diamond.png",
    "five_club.png",
    "six_diamond.png",
    "six_club.png"
]

double_cards_16 = [
    "eight_club.png",   # dealer stops at 17
    "jack_club.png",    # player double
    "three_diamond.png",
    "five_club.png",
    "six_diamond.png",
    "ace_club.png"
]

double_cards_17 = [
    "eight_club.png",   # dealer stops at 17
    "jack_club.png",    # player double
    "three_diamond.png",
    "six_club.png",
    "six_diamond.png",
    "ace_club.png"
]

double_cards_18 = [
    "eight_club.png",   # dealer stops at 17
    "jack_club.png",    # player double
    "three_diamond.png",
    "seven_club.png",
    "six_diamond.png",
    "ace_club.png"
]