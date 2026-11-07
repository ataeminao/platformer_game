"""
ui/main_menu.py - Main menu screen with buttons and animated background.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE, COLOR_BUTTON, COLOR_BUTTON_HOVER

class MainMenu:
    def __init__(self):
        try:
            self.title_font = pygame.font.SysFont("Arial", 54, bold=True)
            self.font = pygame.font.SysFont("Arial", 28, bold=True)
        except Exception:
            self.title_font = pygame.font.Font(None, 60)
            self.font = pygame.font.Font(None, 32)

        self.play_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 300, 300, 50)
        self.level_select_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 380, 300, 50)
        self.instructions_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 460, 300, 50)
        self.quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 540, 300, 50)

    def draw(self, surface: pygame.Surface):
        surface.fill((20, 25, 40))

        # Title
        title = self.title_font.render("CHRONO PLATFORMER ADVENTURE", True, (250, 210, 50))
        surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 150))

        mouse_pos = pygame.mouse.get_pos()

        # Buttons
        for rect, text in [
            (self.play_button, "PLAY GAME"),
            (self.level_select_button, "LEVEL SELECT"),
            (self.instructions_button, "INSTRUCTIONS"),
            (self.quit_button, "QUIT")
        ]:
            color = COLOR_BUTTON_HOVER if rect.collidepoint(mouse_pos) else COLOR_BUTTON
            pygame.draw.rect(surface, color, rect, border_radius=8)
            t_surface = self.font.render(text, True, COLOR_WHITE)
            surface.blit(t_surface, (rect.centerx - t_surface.get_width() // 2, rect.centery - t_surface.get_height() // 2))

    def handle_event(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            if self.play_button.collidepoint(pos):
                return "play"
            elif self.level_select_button.collidepoint(pos):
                return "level_select"
            elif self.instructions_button.collidepoint(pos):
                return "instructions"
            elif self.quit_button.collidepoint(pos):
                return "quit"
        return None