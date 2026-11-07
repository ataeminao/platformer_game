"""
ui/pause_menu.py - Pause menu overlay.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE, COLOR_BUTTON, COLOR_BUTTON_HOVER

class PauseMenu:
    def __init__(self):
        try:
            self.font = pygame.font.SysFont("Arial", 28, bold=True)
        except Exception:
            self.font = pygame.font.Font(None, 32)

        self.resume_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 280, 300, 50)
        self.restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 360, 300, 50)
        self.menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, 440, 300, 50)

    def draw(self, surface: pygame.Surface):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        for rect, text in [
            (self.resume_button, "RESUME"),
            (self.restart_button, "RESTART LEVEL"),
            (self.menu_button, "MAIN MENU")
        ]:
            color = COLOR_BUTTON_HOVER if rect.collidepoint(mouse_pos) else COLOR_BUTTON
            pygame.draw.rect(surface, color, rect, border_radius=8)
            t_surface = self.font.render(text, True, COLOR_WHITE)
            surface.blit(t_surface, (rect.centerx - t_surface.get_width() // 2, rect.centery - t_surface.get_height() // 2))

    def handle_event(self, event) -> str:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            if self.resume_button.collidepoint(pos):
                return "resume"
            elif self.restart_button.collidepoint(pos):
                return "restart"
            elif self.menu_button.collidepoint(pos):
                return "menu"
        return None