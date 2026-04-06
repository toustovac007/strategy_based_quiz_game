from math import floor

from tile import Tile

class Board:
    def __init__(self, players):
        self.tiles = []
        self.heights = []
        self.max_height = 0
        self.players = players
        self.generate_board()

    def generate_board(self):
        self.heights = [3,4,5,6,7,8,7,8,7,8,7,6,5,4,3]
        self.max_height = max(self.heights)

        for col, height in enumerate(self.heights):
            column_tiles = []
            for row in range(height):
                column_tiles.append(Tile(col, row, board=self))
            self.tiles.append(column_tiles)
            print(len(self.tiles[col]))
        print(len(self.tiles))
        self.tiles[0][floor(self.heights[0]/2)].update("blue")
        self.tiles[len(self.heights)-1][floor(self.heights[0]/2)].update("red")

    def set_players(self, players):
        self.players = players

    def get_player_by_color(self, color):
        for p in self.players:
            if p.color == color:
                return p
        return None

