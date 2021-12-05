import random
import os

## FOR : https://adventofcode.com/2021/day/4 ##
class BingoCard():
    def __init__(self, values_range):
        self.values_range = values_range
        self.board = [] # 5 x 5 : [value, marked]

    def set_board(self, board):
        self.board = board  

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
                    if not self.board[j][i][1]:
                        allMarked = False
                        break
                if allMarked:
                    print("BINGO! ( bingo in column",i+1," )")
                    bingo = True
                    break

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
    def __init__(self, number_of_cards, use_input_file):
        self.use_input_file = use_input_file
        self.drawn_numbers = []
        self.bingo_cards = []
        self.number_of_cards = number_of_cards
        self.winners = []

    def read_cards(self):
        file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(file_path) as f:
            lines = f.readlines()
        # remove first 2 lines (numbers and empty line)
        lines = lines[2:]
        # remove empty lines
        lines = [line for line in lines if line != "\n"]
        # grab 5x5 boards and generate new cards with it
        for i in range(int(len(lines)/5)):
            board_lines = lines[i*5:i*5+5]
            board = []
            for line in board_lines:
                line = line.split(" ")
                line = [int(number) for number in line if number != ""]
                new_line = []
                for value in line:
                    new_line.append([value, False])
                board.append(new_line)
            new_card = BingoCard([min(self.drawn_numbers), max(self.drawn_numbers)])
            new_card.set_board(board)
            self.bingo_cards.append(new_card)

    def read_drawn_numbers(self):
        file_path = os.path.join(os.path.dirname(__file__), "input.txt")
        with open(file_path) as f:
            numbers = f.readline().split(',')
        numbers = [int(number) for number in numbers]
        self.drawn_numbers = numbers
    
    def draw_number(self, number):
        final_winner = False
        last_winner = -1
        for card in self.bingo_cards:
            if (self.bingo_cards.index(card) not in self.winners):
                card.mark_number(number)
                if card.check_bingo():
                    self.winners.append(self.bingo_cards.index(card))
                    if (len(self.winners) == len(self.bingo_cards)):
                        final_winner = True
                        last_winner = self.winners[-1]
                        score = card.calculate_score(number)
                        print("Final card at index", self.winners[-1], "finally won!")
                        print("Last winner's score:", score)
        return final_winner

    def play(self):
        if self.use_input_file:
            print("Reading drawing order...")
            self.read_drawn_numbers()
            print("Reading bingo cards...")
            self.read_cards()
        else:
            print("Game started!\nDrawing numbers...")
            self.draw_numbers()
            print("Generating bingo cards...")
            self.generate_cards()
        print("Playing drawn numbers...")
        for number in self.drawn_numbers:
            final_winner = self.draw_number(number)
            if final_winner:
                break

## Main ##
bingo = BingoGame(number_of_cards=10, use_input_file=True)
bingo.play()