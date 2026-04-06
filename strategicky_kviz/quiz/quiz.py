import json
import random
import pygame
import hashlib


class QuizManager:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.questions = json.load(f)

        self.current_question = None
        self.active = False
        self.result = None

        self.time_limit = 10
        self.start_time = 0

    def start_question(self):
        self.current_question = random.choice(self.questions)
        self.active = True
        self.result = None
        self.start_time = pygame.time.get_ticks()

    def hash_text(self, text):
        # sjednocení → zabrání chybám
        return hashlib.sha256(text.strip().lower().encode("utf-8")).hexdigest()

    def answer(self, index):
        if not self.active:
            return

        selected_option = self.current_question["options"][index]
        selected_hash = self.hash_text(selected_option)

        correct_hash = self.current_question["correct_hash"]

        self.result = (selected_hash == correct_hash)
        self.active = False

    def cancel(self):
        self.result = False
        self.active = False

    def update(self):
        if not self.active:
            return

        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000

        if elapsed >= self.time_limit:
            self.result = False
            self.active = False

    def get_time_left(self):
        if not self.active:
            return 0

        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        return max(0, int(self.time_limit - elapsed))