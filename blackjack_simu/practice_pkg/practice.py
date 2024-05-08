''' 
checks the basic strategy for pair splitting 
''' 
def pair_splitting(self, 
                   player_choice, 
                   player_cards, 
                   dealer_cards): 

    # checks for the correct move if player starts with ace's 
    if (player_choice != "split" and 
        player_cards[0].startswith("ace") and 
        player_cards[1].startswith("ace") and 
        (dealer_cards[0].startswith("two") or 
        dealer_cards[0].startswith("three") or 
        dealer_cards[0].startswith("four") or 
        dealer_cards[0].startswith("five") or 
        dealer_cards[0].startswith("six") or 
        dealer_cards[0].startswith("seven") or 
        dealer_cards[0].startswith("eight") or 
        dealer_cards[0].startswith("nine") or 
        dealer_cards[0].startswith("jack") or 
        dealer_cards[0].startswith("queen") or 
        dealer_cards[0].startswith("king") or 
        dealer_cards[0].startswith("ace"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with ten's 
    elif (player_choice == "split" and 
          ((player_cards[0].startswith("jack") and 
          player_cards[1].startswith("jack")) or 
          (player_cards[0].startswith("queen") and 
          player_cards[1].startswith("queen")) or 
          (player_cards[0].startswith("king") and 
          player_cards[1].startswith("king"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 
        
    # checks for the correct move if player starts with nine's 
    elif (player_choice != "split" and 
          player_cards[0].startswith("nine") and 
          player_cards[1].startswith("nine") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    elif (player_choice == "split" and 
          player_cards[0].startswith("nine") and 
          player_cards[1].startswith("nine") and 
          (dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move)    

    # checks for the correct move if player starts with eight's 
    elif (player_choice != "split" and 
          player_cards[0].startswith("eight") and 
          player_cards[1].startswith("eight") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with seven's 
    elif (player_choice != "split" and 
          player_cards[0].startswith("seven") and 
          player_cards[1].startswith("seven") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    elif (player_choice == "split" and 
          player_cards[0].startswith("seven") and 
          player_cards[1].startswith("seven") and 
          (dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with six's 
    elif (player_choice != "split" and 
          player_cards[0].startswith("six") and 
          player_cards[1].startswith("six") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    elif (player_choice == "split" and 
          player_cards[0].startswith("six") and 
          player_cards[1].startswith("six") and 
          (dealer_cards[0].startswith("seven") or
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))):

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with five's 
    elif (player_choice == "split" and 
          player_cards[0].startswith("five") and 
          player_cards[1].startswith("five") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with four's 
    elif (player_choice == "split" and 
          player_cards[0].startswith("four") and 
          player_cards[1].startswith("four") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 

    elif (player_choice != "split" and 
          player_cards[0].startswith("four") and 
          player_cards[1].startswith("four") and 
          (dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with three's 
    elif (player_choice != "split" and 
          player_cards[0].startswith("three") and 
          player_cards[1].startswith("three") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    elif (player_choice == "split" and 
          player_cards[0].startswith("three") and 
          player_cards[1].startswith("three") and 
          (dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with two's 
    elif (player_choice != "split" and 
          player_cards[0].startswith("two") and 
          player_cards[1].startswith("two") and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven"))): 

        text_label = "split message label" 
        correct_move = "split" 
        print("Correct move:", correct_move) 

    elif (player_choice == "split" and 
          player_cards[0].startswith("two") and 
          player_cards[1].startswith("two") and 
          (dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "no split message label" 
        correct_move = "no split" 
        print("Correct move:", correct_move) 

''' 
checks the basic strategy for soft totals 
''' 
def soft_totals(self, 
                player_choice, 
                player_cards, 
                dealer_cards): 

    # checks for the correct move if player starts with an ace or nine 
    if (player_choice != "stand" and 
        ((player_cards[0].startswith("ace") and 
        player_cards[1].startswith("nine")) or 
        (player_cards[0].startswith("nine") and 
        player_cards[1].startswith("ace"))) and 
        (dealer_cards[0].startswith("two") or 
        dealer_cards[0].startswith("three") or 
        dealer_cards[0].startswith("four") or 
        dealer_cards[0].startswith("five") or 
        dealer_cards[0].startswith("six") or 
        dealer_cards[0].startswith("seven") or 
        dealer_cards[0].startswith("eight") or 
        dealer_cards[0].startswith("nine") or 
        dealer_cards[0].startswith("jack") or 
        dealer_cards[0].startswith("queen") or 
        dealer_cards[0].startswith("king") or 
        dealer_cards[0].startswith("ace"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or eight 
    elif (player_choice != "stand" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("eight")) or 
          (player_cards[0].startswith("eight") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("eight")) or 
          (player_cards[0].startswith("eight") and 
          player_cards[1].startswith("ace"))) and 
          dealer_cards[0].startswith("six")): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or seven 
    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("seven")) or 
          (player_cards[0].startswith("seven") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "stand" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("seven")) or 
          (player_cards[0].startswith("seven") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move)  

    elif (player_choice != "hit" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("seven")) or 
          (player_cards[0].startswith("seven") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or six 
    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("six")) or 
          (player_cards[0].startswith("six") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          ((player_cards[0].startswith("ace") and
          player_cards[1].startswith("six")) or
          (player_cards[0].startswith("six") and
          player_cards[1].startswith("ace"))) and
          (dealer_cards[0].startswith("two") or
          dealer_cards[0].startswith("seven") or
          dealer_cards[0].startswith("eight") or
          dealer_cards[0].startswith("nine") or
          dealer_cards[0].startswith("jack") or
          dealer_cards[0].startswith("queen") or
          dealer_cards[0].startswith("king") or
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or five 
    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("five")) or 
          (player_cards[0].startswith("five") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("five")) or 
          (player_cards[0].startswith("five") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or four 
    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("four")) or 
          (player_cards[0].startswith("four") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("four")) or 
          (player_cards[0].startswith("four") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or three 
    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("three")) or 
          (player_cards[0].startswith("three") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("three")) or 
          (player_cards[0].startswith("three") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player starts with an ace or two 
    elif (player_choice != "double" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("two")) or 
          (player_cards[0].startswith("two") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          ((player_cards[0].startswith("ace") and 
          player_cards[1].startswith("two")) or 
          (player_cards[0].startswith("two") and 
          player_cards[1].startswith("ace"))) and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

''' 
checks the basic strategy for hard totals 
''' 
def hard_totals(self, 
                player_choice, 
                player_total, 
                dealer_cards): 

    # checks for the correct move if player's total is 17 
    if (player_choice != "stand" and 
        player_total == 17 and 
        (dealer_cards[0].startswith("two") or 
        dealer_cards[0].startswith("three") or 
        dealer_cards[0].startswith("four") or 
        dealer_cards[0].startswith("five") or 
        dealer_cards[0].startswith("six") or 
        dealer_cards[0].startswith("seven") or 
        dealer_cards[0].startswith("eight") or 
        dealer_cards[0].startswith("nine") or 
        dealer_cards[0].startswith("jack") or 
        dealer_cards[0].startswith("queen") or 
        dealer_cards[0].startswith("king") or 
        dealer_cards[0].startswith("ace"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 16 
    elif (player_choice != "stand" and 
          player_total == 16 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          player_total == 16 and 
          (dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 15 
    elif (player_choice != "stand" and 
          player_total == 15 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          player_total == 15 and 
          (dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 14 
    elif (player_choice != "stand" and 
          player_total == 14 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          player_total == 14 and 
          (dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 13 
    elif (player_choice != "stand" and 
          player_total == 13 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move)

    elif (player_choice != "hit" and 
          player_total == 13 and 
          (dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 12 
    elif (player_choice != "stand" and 
          player_total == 12 and 
          (dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "stand message label" 
        correct_move = "stand" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          player_total == 12 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 11 
    elif (player_choice != "double" and 
          player_total == 11 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 10 
    elif (player_choice != "double" and 
          player_total == 10 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          player_total == 10 and 
          (dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 9 
    elif (player_choice != "double" and 
          player_total == 9 and 
          (dealer_cards[0].startswith("three") or 
          dealer_cards[0].startswith("four") or 
          dealer_cards[0].startswith("five") or 
          dealer_cards[0].startswith("six"))): 

        text_label = "double message label" 
        correct_move = "double" 
        print("Correct move:", correct_move) 

    elif (player_choice != "hit" and 
          player_total == 9 and 
          (dealer_cards[0].startswith("two") or 
          dealer_cards[0].startswith("seven") or 
          dealer_cards[0].startswith("eight") or 
          dealer_cards[0].startswith("nine") or 
          dealer_cards[0].startswith("jack") or 
          dealer_cards[0].startswith("queen") or 
          dealer_cards[0].startswith("king") or 
          dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move) 

    # checks for the correct move if player's total is 8 or less 
    if (player_choice != "hit" and 
        player_total <= 8 and 
        (dealer_cards[0].startswith("two") or 
        dealer_cards[0].startswith("three") or 
        dealer_cards[0].startswith("four") or 
        dealer_cards[0].startswith("five") or 
        dealer_cards[0].startswith("six") or 
        dealer_cards[0].startswith("seven") or 
        dealer_cards[0].startswith("eight") or 
        dealer_cards[0].startswith("nine") or 
        dealer_cards[0].startswith("jack") or 
        dealer_cards[0].startswith("queen") or 
        dealer_cards[0].startswith("king") or 
        dealer_cards[0].startswith("ace"))): 

        text_label = "hit message label" 
        correct_move = "hit" 
        print("Correct move:", correct_move)