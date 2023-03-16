from Board import Board
from Workspace import Workspace

class Game:
    def __init__(self, board_rows, board_columns, bird_start_position, pig_position):
        self.board = Board(board_rows, board_columns, bird_start_position, pig_position)
        self.workspace = Workspace()

    def run(self):
        gameIsrunning = True
        self.board.display_board()
        self.workspace.display_instructions()
        while gameIsrunning:
            command = input('move: ')
            if command == 'q':
                gameIsrunning = False
                self.game_over()
            else:
                self.board.bird.move(command)
    
    def game_over(self):
        if self.board.bird.current_position == self.board.pig.position:
            print(self.board.bird.game_over(True))
            print(self.board.pig.game_over(False))
        else:
            print(self.board.bird.game_over(False))
            print(self.board.pig.game_over(True))                                            

game = Game(10, 10, (1, 2), (7, 7))
game.run()