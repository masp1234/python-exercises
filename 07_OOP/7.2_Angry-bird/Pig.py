class Pig:
    def __init__(self, position):
        self.position = position

    def game_over(self, has_won):
        end_position = f'The pig was on {self.position}'
        if has_won:
            return f'The pig has won. {end_position}'
        return f'The pig has lost. {end_position}'