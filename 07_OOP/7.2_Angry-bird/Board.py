from Bird import Bird
from Pig import Pig

class Board:
    def __init__(self, rows, columns, bird_start_position, pig_position):
        self.bird = Bird(bird_start_position, 'f')
        self.pig = Pig(pig_position)
        self.board = [[(row, column) for column in range(columns)] for row in range(rows)]

    def __str__(self):
        representation = ''
        for row in self.board:
            for column in row:
                if self.bird.current_position == column:
                    representation += 'B '
                elif self.pig.position == column:
                    representation += 'P '
                else:
                    representation += '* '
            representation += '\n'
        return representation

    def display_board(self):
        print(self)
