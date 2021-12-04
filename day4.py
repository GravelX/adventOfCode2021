import random

## FOR : https://adventofcode.com/2021/day/4 ##
class BingoCard():
    def __init__(self, values_range):
        self.values_range = values_range
        self.board = [] # 5 x 5 : [value, marked]

    def fill_board(self):
        card_values = random.sample(range(self.values_range[0], self.values_range[1]), 25)
        for i in range(5):
            line = []
            for j in range(5):
                line.append([card_values[(i*5)+(j)], False])
            self.board.append(line)            

    def mark_number(self, number):
        for line in self.board:
            for case in line:
                if case[0] == number:
                    case[1] = True

    def check_bingo(self):
        bingo = False
        # lines
        for k,line in enumerate(self.board):
            allMarked = True
            for case in line:
                if not case[1]:
                    allMarked = False
                    break
            if allMarked:
                print("BINGO! ( bingo in line",k+1,")")
                bingo = True
                break
        # columns
        if not bingo:
            for i in range(5):
                allMarked = True
                for j in range(5):
                    if not self.board[i][j][1]:
                        allMarked = False
                        break
                if allMarked:
                    print("BINGO! ( bingo in column",j+1," )")
                    bingo = True
                    break
        # diagonals
        if not bingo:
            # diagonale 1
            allMarked = True
            for i in range(5):
                if not self.board[i][i][1]:
                    allMarked = False
                    break
            if allMarked:
                print("BINGO! ( bingo in diagonal \\ )")
                bingo = True
            # diagonale 2
            if not bingo:
                allMarked = True
                for i in range(5):
                    if not self.board[i][4-i][1]:
                        allMarked = False
                        break
                if allMarked:
                    print("BINGO! ( bingo in diagonal / )")
                    bingo = True

        return bingo

    def calculate_score(self, last_called):
        score = 0
        for line in self.board:
            for case in line:
                if not case[1]:
                    score += case[0]
        score = score * last_called

        return score

    def print_board(self):
        for line in self.board:
            for case in line:
                if not case[1]:
                    print("{:4s}".format(str(case[0])), end=" ")
                else :
                    print("[{:2s}]".format(str(case[0])), end=" ")
            print()
        print("-------------")

class BingoGame():
    def __init__(self, number_of_cards):
        self.drawn_numbers = []
        self.bingo_cards = []
        self.number_of_cards = number_of_cards

    def draw_numbers(self):
        numbers = random.sample(range(0, 100), 99)
        print("Numbers will be drawn in the following order:\n",numbers)
        self.drawn_numbers = numbers

    def generate_cards(self):
        for i in range(self.number_of_cards):
            new_card = BingoCard([min(self.drawn_numbers), max(self.drawn_numbers)])
            new_card.fill_board()
            self.bingo_cards.append(new_card)
        print("Here are the",self.number_of_cards,"cards generated:")
        for card in self.bingo_cards:
            card.print_board()
    
    def draw_number(self, number):
        winner = False
        for card in self.bingo_cards:
            card.mark_number(number)
            if card.check_bingo():
                winner = True
                print("Card at index", self.bingo_cards.index(card), "won!")
                winning_numbers = self.drawn_numbers[:self.drawn_numbers.index(number)+1]
                print("Numbers drawn before win:",winning_numbers)
                card.print_board()
                score = card.calculate_score(number)
                print("Winner's score:", score)
        return winner

    def play(self):
        print("Game started!\nDrawing numbers...")
        self.draw_numbers()
        print("Generating bingo cards...")
        self.generate_cards()
        print("Playing drawn numbers...")
        for number in self.drawn_numbers:
            winner = self.draw_number(number)
            if winner:
                break

## Main ##
bingo = BingoGame(number_of_cards=10)
bingo.play()