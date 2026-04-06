from math import floor

import pygame
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
info = pygame.display.Info()

HEX_SIZE = floor(info.current_h / 17.25)

HEX_WIDTH = HEX_SIZE * 2
HEX_HEIGHT = math.sqrt(3) * HEX_SIZE

HORIZONTAL_SPACING = HEX_SIZE * 1.6

VERTICAL_SPACING = (HEX_HEIGHT + HEX_SIZE + 10)/1.7



class Renderer:
    def __init__(self, screen, board, players):
        self.screen = screen
        self.board = board
        self.font = pygame.font.SysFont(None, 48)

        self.players = players

        pygame.init()
        info = pygame.display.Info()
        self.screen_width_offset, self.screen_height_offset = info.current_w/8, info.current_h/50



    def draw_hex(self, x, y, size, color):
        points = []
        for i in range(6):
            angle = math.radians(60 * i) # + 30 pro otočení o 90 stupnů
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))

        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, BLACK, points, 2)

    def draw_action_points(self, action_points):
        # vykreslení textu
        text = self.font.render(str(action_points), True, (255, 255, 255))

        # levý horní roh (modrý)
        x = self.screen.get_width()/2 - text.get_width() - 20
        self.screen.blit(text, (x, 20))



    def draw(self, action_points):
        self.screen.fill((30, 30, 30))

        self.draw_action_points(action_points)

        for col_index, column in enumerate(self.board.tiles):
            for row_index, tile in enumerate(column):



                x = col_index * HORIZONTAL_SPACING + self.screen_width_offset

                y_offset = (10 - len(column)) * VERTICAL_SPACING * 0.5
                y = row_index * VERTICAL_SPACING + y_offset + self.screen_height_offset

                tile_color = self.board.tiles[col_index][row_index].color
                self.draw_hex(x, y, HEX_SIZE, tile_color)

        self.draw_score(self.players)



    def get_hex_position(self, col_index, row, column_height):

        x = col_index * HORIZONTAL_SPACING + self.screen_width_offset
        y_offset = (10 - column_height) * HORIZONTAL_SPACING * 0.5
        y = row * VERTICAL_SPACING + y_offset + self.screen_height_offset

        return x, y



    def draw_quiz_popup(self, quiz_manager):
        if not quiz_manager.active:
            return

        # pozadí popupu
        popup_rect = pygame.Rect(200, 150, 600, 400)
        pygame.draw.rect(self.screen, (240, 240, 240), popup_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), popup_rect, 3)

        question = quiz_manager.current_question

        # text otázky
        text = self.font.render(question["question"], True, (0, 0, 0))
        self.screen.blit(text, (popup_rect.x + 20, popup_rect.y + 20))

        # tlačítka odpovědí
        self.answer_buttons = []

        for i, option in enumerate(question["options"]):
            btn_rect = pygame.Rect(
                popup_rect.x + 50,
                popup_rect.y + 80 + i * 70,
                500,
                50
            )

            pygame.draw.rect(self.screen, (200, 200, 200), btn_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), btn_rect, 2)

            txt = self.font.render(option, True, (0, 0, 0))
            self.screen.blit(txt, (btn_rect.x + 10, btn_rect.y + 10))

            self.answer_buttons.append((btn_rect, i))

        # tlačítko zavřít (X)
        self.close_button = pygame.Rect(
            popup_rect.right - 40,
            popup_rect.y + 10,
            30,
            30
        )

        pygame.draw.rect(self.screen, (255, 100, 100), self.close_button)
        pygame.draw.rect(self.screen, (0, 0, 0), self.close_button, 2)

        x_text = self.font.render("X", True, (0, 0, 0))
        self.screen.blit(x_text, (self.close_button.x + 5, self.close_button.y))


        time_left = quiz_manager.get_time_left()
        color = (0, 0, 0)
        if time_left <= 3:
            color = (255, 0, 0)

        timer_text = self.font.render(f"{time_left}s", True, color)
        self.screen.blit(timer_text, (
            popup_rect.centerx - 20,
            popup_rect.y + pygame.display.Info().current_h//2.2
        ))

    def draw_score(self, players):
        font = pygame.font.SysFont(None, 40)

        red = next(p for p in players if p.color == "red")
        blue = next(p for p in players if p.color == "blue")

        red_text = font.render(f"RED: {red.score}", True, (255, 0, 0))
        blue_text = font.render(f"BLUE: {blue.score}", True, (0, 0, 255))

        # levý horní roh
        self.screen.blit(red_text, (20, 20))

        # pravý horní roh
        self.screen.blit(blue_text, (
            self.screen.get_width() - blue_text.get_width() - 20,
            20
        ))