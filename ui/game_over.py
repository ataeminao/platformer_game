"""
ui/game_over.py - Game Over screen.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE, COLOR_BUTTON, COLOR_BUTTON_HOVER

class GameOverScreen:
    def __init__(self):
        try:
            self.title_font = pygame.font.SysFont("Arial", 50, bold=True)
            self.font = pygame.font.SysFont("Arial", 28, bold=True)
        except Exception:
            self.title_font = pygame.font.Font(None, 50)
            self.font = pygame.font.Font(None, 32)

        self.restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 400, 300, 50)
        self.menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 480, 300, 50)

    def draw(self, surface: pygame.Surface, score: int):
        surface.fill((30, 10, 15))
        title = self.title_font.render("GAME OVER", True, (240, 60, 60))
        score_text = self.font.render(f"Final Score: {score}", True, COLOR_WHITE)

        surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        surface.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 280))

        mouse_pos = pygame.mouse.get_pos()
        for rect, text in [
            (self.restart_button, "TRY AGAIN"),
            (self.menu_button, "MAIN MENU")
        ]:
            color = COLOR_BUTTON_HOVER if rect.collidepoint(mouse_pos) else COLOR_BUTTON
            pygame.draw.rect(surface, color, rect, border_radius=8)
            t_surface = self.font.render(text, True, COLOR_WHITE)
            surface.blit(t_surface, (rect.centerx - t_surface.get_width() // 2, rect.centery - t_surface.get_height() // 2))

    def handle_event(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            if self.restart_button.collidepoint(pos):
                return "restart"
            elif self.menu_button.collidepoint(pos):
                return "menu"
        return None