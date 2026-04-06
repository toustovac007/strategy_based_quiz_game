from math import floor
from time import sleep

import pygame
from board import Board
from quiz.quiz import QuizManager
from ui.renderer import Renderer

from player import Player
from systems.turn_manager import TurnManager
from ui.input_handler import InputHandler

from quiz.quiz import QuizManager

class Game:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        screen_width, screen_height = info.current_w, info.current_h
        screen_shrink = 0.93
        self.screen = pygame.display.set_mode((screen_width, screen_height * screen_shrink))
        pygame.display.set_caption("Hex Quiz Strategy")

        print(f"Rozlišení displeje: {screen_width}x{screen_height}")

        self.players = [
            Player(1, "red"),    #(255, 0, 0)
            Player(2, "blue")     #(0, 0, 255)
        ]
        
        self.current_player = self.players[0]

        self.winner = None

        self.turn_manager = TurnManager(self.players)
        self.pending_tile = None

        self.board = Board(self.players)
        self.renderer = Renderer(self.screen, self.board, self.players)
        self.input_handler = InputHandler(self.board, self.renderer)

        self.board.set_players(self.players)

        self.quiz_manager = QuizManager("./data/questions_hashed.json")

        self.clock = pygame.time.Clock()


        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quiz_manager.active:
                    self.input_handler.handle_quiz_click(pygame.mouse.get_pos(), self.quiz_manager, self.renderer)
                else:

                    if self.pending_tile and self.quiz_manager.result is None:
                        self.pending_tile = None

                    tile = self.input_handler.get_tile_at_pos(pygame.mouse.get_pos())
                    if tile:
                        print(f"Kliknuto na tile: col={tile.col}, row={tile.row}")


                        self.current_player = self.turn_manager.get_current_player()

                        print(tile.can_be_activated(self.current_player))

                        if tile.can_be_activated(self.current_player):
                            self.quiz_manager.start_question()
                            self.pending_tile = tile  # uložíš si tile



    def update(self):
        self.quiz_manager.update()
        if self.quiz_manager.result is not None and self.pending_tile:
            if self.quiz_manager.result:
                self.pending_tile.update(self.current_player.color)
                self.pending_tile.check_neighbours_after_taking_control()
                self.turn_manager.use_action()
            else:
                self.pending_tile.locked = True
                self.turn_manager.use_action()


            self.pending_tile = None
            self.quiz_manager.result = None

        winner = self.check_for_win()
        if winner:
            self.winner = winner

    def render(self):
        if self.winner:
            self.draw_victory_screen()
        else:
            self.renderer.draw(self.turn_manager.actions_left)
            self.renderer.draw_quiz_popup(self.quiz_manager)

        pygame.display.flip()
        self.clock.tick(60)



    def check_for_win(self):
        for player in self.players:
            if player.score >= 30:
                return player.color
        if self.board.tiles[0][(self.board.heights[0]//2)].owner == "red":
            return "red"
        elif self.board.tiles[len(self.board.heights)-1][(self.board.heights[0]//2)].owner == "blue":
            return "blue"
        else:
            return None

    def draw_victory_screen(self):
        self.screen.fill((255, 255, 255))

        font_big = pygame.font.SysFont(None, 120)
        font_small = pygame.font.SysFont(None, 60)

        text = font_big.render("VÍTĚZSTVÍ", True, (0, 0, 0))

        winner_text = font_small.render(
            f"Vyhrál {self.winner}",
            True,
            (255, 0, 0) if self.winner == "red" else (0, 0, 255)
        )

        self.screen.blit(text, text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50)))
        self.screen.blit(winner_text, winner_text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50)))