"""
core/game.py - Main game coordinator and state machine.
"""

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_SKY_TOP, COLOR_SKY_BOTTOM
from core.game_state import GameState
from core.camera import Camera
from core.level_manager import LevelManager
from entities.player import Player
from systems.audio import AudioManager
from systems.scoring import ScoringSystem
from systems.save_system import SaveSystem
from ui.hud import HUD
from ui.main_menu import MainMenu
from ui.pause_menu import PauseMenu
from ui.game_over import GameOverScreen
from ui.victory_screen import VictoryScreen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chrono Platformer Adventure")
        self.clock = pygame.time.Clock()
        
        self.state = "MENU"  # MENU, PLAYING, PAUSED, GAME_OVER, VICTORY, LEVEL_SELECT
        self.game_state = GameState()
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level_manager = LevelManager()
        self.audio_manager = AudioManager()
        
        self.hud = HUD()
        self.main_menu = MainMenu()
        self.pause_menu = PauseMenu()
        self.game_over_screen = GameOverScreen()
        self.victory_screen = VictoryScreen()
        
        self.current_level = None
        self.player = None
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "MENU":
                action = self.main_menu.handle_event(event)
                if action == "play":
                    self.start_level(1)
                elif action == "quit":
                    self.running = False
            elif self.state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_p):
                        self.state = "PAUSED"
                    
            elif self.state == "PAUSED":
                action = self.pause_menu.handle_event(event)
                if action == "resume":
                    self.state = "PLAYING"
                elif action == "restart":
                    self.start_level(self.game_state.current_level)
                    self.state = "PLAYING"
                elif action == "menu":
                    self.state = "MENU"
            elif self.state == "GAME_OVER":
                action = self.game_over_screen.handle_event(event)
                if action == "restart":
                    self.game_state.reset_game()
                    self.start_level(1)
                elif action == "menu":
                    self.state = "MENU"
            elif self.state == "VICTORY":
                action = self.victory_screen.handle_event(event)
                if action == "menu":
                    self.state = "MENU"

    def update(self):
        if self.state == "PLAYING":
            keys = pygame.key.get_pressed()
            self.current_level.update(self.player.rect)
            self.player.update(keys, self.current_level.platforms)
            self.camera.update(self.player.rect, self.current_level.width, self.current_level.height)

            # Check enemy collisions
            for enemy in self.current_level.enemies:
                if self.player.rect.colliderect(enemy.rect):
                    if self.player.take_damage(10, self.audio_manager):
                        self.game_state.health -= 10
                        if self.game_state.health <= 0:
                            self.game_state.lives -= 1
                            self.game_state.health = 100
                            if self.game_state.lives <= 0:
                                self.state = "GAME_OVER"
                            else:
                                self.start_level(self.game_state.current_level)

            # Check hazard collisions
            for hazard in self.current_level.hazards:
                if self.player.rect.colliderect(hazard.rect):
                    if self.player.take_damage(20, self.audio_manager):
                        self.game_state.health -= 20
                        if self.game_state.health <= 0:
                            self.game_state.lives -= 1
                            self.game_state.health = 100
                            if self.game_state.lives <= 0:
                                self.state = "GAME_OVER"
                            else:
                                self.start_level(self.game_state.current_level)

            # Check projectile collisions
            for proj in self.current_level.projectiles:
                if self.player.rect.colliderect(proj.rect):
                    proj.kill()
                    if self.player.take_damage(15, self.audio_manager):
                        self.game_state.health -= 15
                        if self.game_state.health <= 0:
                            self.game_state.lives -= 1
                            self.game_state.health = 100
                            if self.game_state.lives <= 0:
                                self.state = "GAME_OVER"
                            else:
                                self.start_level(self.game_state.current_level)

            # Check boss collisions
            if self.current_level.boss and self.player.rect.colliderect(self.current_level.boss.rect):
                if self.player.take_damage(15, self.audio_manager):
                    self.game_state.health -= 15

            # Check collectible pickups
            collected = pygame.sprite.spritecollide(self.player, self.current_level.collectibles, True)
            for item in collected:
                self.game_state.score += 100
                self.game_state.collectibles_collected += 1
                if item.item_type == "heart":
                    self.game_state.health = min(100, self.game_state.health + 25)
                self.audio_manager.play_coin()

            # Check fall death
            if self.player.rect.top > self.current_level.height:
                self.game_state.lives -= 1
                self.audio_manager.play_hurt()
                if self.game_state.lives <= 0:
                    self.state = "GAME_OVER"
                else:
                    self.start_level(self.game_state.current_level)

            # Check exit reached
            if self.player.rect.colliderect(self.current_level.exit_rect):
                if self.game_state.current_level >= 10:
                    self.state = "VICTORY"
                else:
                    self.start_level(self.game_state.current_level + 1)

    def render(self):
        self.screen.fill(COLOR_SKY_TOP)

        if self.state == "MENU":
            self.main_menu.draw(self.screen)
        elif self.state in ("PLAYING", "PAUSED"):
            # Render Level Background
            pygame.draw.rect(self.screen, COLOR_SKY_BOTTOM, (0, 300, SCREEN_WIDTH, SCREEN_HEIGHT - 300))

            # Render Platforms
            for platform in self.current_level.platforms:
                if platform.is_active:
                    self.screen.blit(platform.image, self.camera.apply(platform.rect))

            # Render Hazards
            for hazard in self.current_level.hazards:
                self.screen.blit(hazard.image, self.camera.apply(hazard.rect))

            # Render Collectibles
            for item in self.current_level.collectibles:
                self.screen.blit(item.image, self.camera.apply(item.rect))

            # Render Enemies
            for enemy in self.current_level.enemies:
                self.screen.blit(enemy.image, self.camera.apply(enemy.rect))

            # Render Boss
            if self.current_level.boss:
                self.screen.blit(self.current_level.boss.image, self.camera.apply(self.current_level.boss.rect))

            # Render Projectiles
            for proj in self.current_level.projectiles:
                self.screen.blit(proj.image, self.camera.apply(proj.rect))

            # Render Exit
            pygame.draw.rect(self.screen, (50, 220, 50), self.camera.apply(self.current_level.exit_rect), border_radius=6)

            # Render Player
            self.screen.blit(self.player.image, self.camera.apply(self.player.rect))

            # Render HUD
            self.hud.draw(self.screen, self.game_state)

            if self.state == "PAUSED":
                self.pause_menu.draw(self.screen)
        elif self.state == "GAME_OVER":
            self.game_over_screen.draw(self.screen, self.game_state.score)
        elif self.state == "VICTORY":
            self.victory_screen.draw(self.screen, self.game_state.score)

        pygame.display.flip()

    def start_level(self, level_num: int):
        self.game_state.current_level = level_num
        self.game_state.reset_level_stats()
        self.current_level = self.level_manager.load_level(level_num)
        self.player = Player(self.current_level.player_spawn[0], self.current_level.player_spawn[1])
        self.state = "PLAYING"