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