class Bird:
    def __init__(self, current_position, current_direction):
        self.current_position = current_position
        self.current_direction = current_direction

    def move(self, direction):
        match direction:
            case 'f':
                self.current_position = (self.current_position[0], self.current_position[1] + 1)
            case 'b':
                self.current_position = (self.current_position[0], self.current_position[1] - 1)
            case 'l':
                self.current_position = (self.current_position[0] - 1, self.current_position[1])
            case 'r':
                self.current_position = (self.current_position[0] + 1, self.current_position[1])
            case _:
                pass
                
    def game_over(self, has_won):
        end_position = f'The bird was on position: {self.current_position}'
        if has_won:
            return f'The Bird has won. {end_position}'
        return f'The Bird has lost. {end_position}'
