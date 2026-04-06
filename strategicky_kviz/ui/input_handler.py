import math

class InputHandler:
    def __init__(self, board, renderer):
        self.board = board
        self.renderer = renderer

    def get_tile_at_pos(self, mouse_pos):
        mx, my = mouse_pos

        closest_tile = None
        min_dist = float("inf")

        for row in range(self.board.max_height):
            for col_index, column in enumerate(self.board.tiles):

                if row < len(column):
                    tile = column[row]

                    # STEJNÝ výpočet jako v rendereru
                    x, y = self.renderer.get_hex_position(col_index, row, len(column))

                    dist = math.hypot(mx - x, my - y)

                    if dist < min_dist:
                        min_dist = dist
                        closest_tile = tile

        return closest_tile

    def handle_quiz_click(self, pos, quiz_manager, renderer):
        if not quiz_manager.active:
            return

        # Kontrola kliknutí na odpovědi
        if hasattr(renderer, "answer_buttons") and renderer.answer_buttons:
            for rect, index in renderer.answer_buttons:
                if rect.collidepoint(pos):
                    print(f"Kliknuto na odpověď {index}")  # Debug
                    quiz_manager.answer(index)
                    return

        # Kontrola kliknutí na tlačítko zavřít (X)
        if hasattr(renderer, "close_button") and renderer.close_button.collidepoint(pos):
            print("Kliknuto na zavřít")  # Debug
            quiz_manager.cancel()