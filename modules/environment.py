


class Environment:
    def __init__(self, p1):
        # get players' boards
        self.players = [p1]
        self.num_turns = 0

    def _check_shot(self, defender=None, coordinate=None):
        # check if player i has guessed right
        #returns
        golden_f=0 #for the correct position and color
        silver_f=0 #for the correct color
        check_board=list(self.players[0].info['board'])
        print(check_board, 'javab')
        guess=list(self.players[0].shoot(4))
        print(guess, 'hads')
        for i in range(4):
            if check_board[i]==guess[i]:
                golden_f +=1
                check_board[i]=0
        for i in range(4):
            try:
                position=check_board.index(guess[i])
                silver_f +=1
                check_board[position]=0
            except ValueError:
                    pass
        return golden_f,silver_f   

    def play_turn(self, shooter=None, coordinate=None,iteration=None):
        self.num_turns += 1
        flag=self._check_shot() #first item is golden flag , second item is silver
        if flag[0]==4:
            return 1
        if self.num_turns==iteration:
            return 0
        print('Golden flags: ',flag[0], 'Silver flags: ',flag[1])
        return 2

    def launch_game(self, iterations=10):
        win_flag=2
        while win_flag==2:
            win_flag=self.play_turn(iterations)
        if win_flag==1:
            print("Congrats! you Won")
        else:
            print("Oops, you're out of guesses!")