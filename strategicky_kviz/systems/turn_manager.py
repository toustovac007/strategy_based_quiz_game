class TurnManager:
    def __init__(self, players, actions_per_turn=3):
        self.players = players
        self.current_index = 0
        self.actions_per_turn = actions_per_turn
        self.actions_left = actions_per_turn

    def get_current_player(self):
        return self.players[self.current_index]

    def use_action(self):
        self.actions_left -= 1
        if self.actions_left == 0:
            self.end_turn()

    def end_turn(self):
        self.current_index = (self.current_index + 1) % len(self.players)
        self.actions_left = self.actions_per_turn