class Tile:
    def __init__(self, col, row, board):
        self.col = col
        self.row = row
        self.owner = None
        self.board = board
        self.color = (255, 255, 255) if self.owner is None else ((0, 0, 255) if self.owner == "blue" else (255, 0, 0))

    def update(self, new_owner):
        old_owner = self.owner

        if old_owner == new_owner:
            return

        # odečti starému hráči
        if old_owner is not None:
            player = self.board.get_player_by_color(old_owner)
            if player:
                player.score -= 1

        # přičti novému hráči
        if new_owner is not None:
            player = self.board.get_player_by_color(new_owner)
            if player:
                player.score += 1

        self.owner = new_owner
        self.color = (255, 255, 255) if self.owner is None else (
            (0, 0, 255) if self.owner == "blue" else (255, 0, 0)
        )

    def get_neighbors(self):
            neighbors = []
            col = self.col
            row = self.row
            board = self.board

            directions = [
                (0, -1), (0, 1),  # nahoře/dole
            ]

            # levý sloupec
            if col - 1 >= 0:
                if len(board.tiles[col - 1]) < len(board.tiles[col]):
                    directions += [(-1, -1), (-1, 0)]
                else:
                    directions += [(-1, 0), (-1, 1)]

            # pravý sloupec
            if col + 1 < len(board.tiles):
                if len(board.tiles[col + 1]) > len(board.tiles[col]):
                    directions += [(1, 0), (1, 1)]
                else:
                    directions += [(1, -1), (1, 0)]

            for dc, dr in directions:
                nc = col + dc
                nr = row + dr

                if 0 <= nc < len(board.tiles):
                    if 0 <= nr < len(board.tiles[nc]):
                        neighbors.append(board.tiles[nc][nr])

            return neighbors

    def check_for_controlled_neighbours(self, condition=4):
        neighbors = self.get_neighbors()

        owners = [n.owner for n in neighbors if n.owner is not None]

        if owners.count("red") >= condition:
            self.update("red")
        elif owners.count("blue") >= condition:
            self.update("blue")

    def check_neighbours_after_taking_control(self):
        for neighbor in self.get_neighbors():
            neighbor.check_for_controlled_neighbours()

    def can_be_activated(self, player):
        # nesmí být už zabraný
        if self.owner == player:
            return False

        # alespoň jeden soused musí patřit hráči
        for neighbor in self.get_neighbors():
            if neighbor.owner == player.color:
                return True

        return False