import random

class Player:
    def __init__(self, name=None):
        self.info = {
            'name': name,
            'board': random_board_creator()
        }

    def shoot(self,board_size):
        #each turn the player guesses the sequel
        while True:
            guess=input("Guess your 4 digit sequel: ")
            if len(guess)== board_size:
                break
        return guess
def random_board_creator(board_size=4):
    #creating human player target board randomly
    #current board size is 4
    colors=['r','g','b','y','w','p']
    board=[]
    while len(board)<board_size:
        board.append(random.choice(colors))
    return board
