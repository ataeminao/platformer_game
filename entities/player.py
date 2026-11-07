import pygame
import math
from settings import (
    COLOR_PLAYER, COLOR_PLAYER_DMG, PLAYER_SPEED, 
    PLAYER_JUMP_FORCE, PLAYER_ACCELERATION, PLAYER_FRICTION
)
from systems.physics import apply_gravity
from systems.audio import AudioManager

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 40
        self.height = 54
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.audio_manager = AudioManager()
        
        self.x = float(x)
        self.y = float(y)
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        
        self.is_grounded = False
        self.facing_right = True
        self.invulnerable_timer = 0.0
        self.animation_timer = 0.0
        
        self.state = "idle"  # idle, running, jumping, falling, hurt

    def update(self, keys, platforms):
        # Horizontal movement input
        accel = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            accel = -PLAYER_ACCELERATION
            self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            accel = PLAYER_ACCELERATION
            self.facing_right = True
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.jump(self.audio_manager)

        if accel != 0:
            self.velocity_x += accel
            self.velocity_x = max(-PLAYER_SPEED, min(PLAYER_SPEED, self.velocity_x))
        else:
            self.velocity_x *= PLAYER_FRICTION
            if abs(self.velocity_x) < 0.1:
                self.velocity_x = 0.0

        # Apply gravity
        self.velocity_y = apply_gravity(self.velocity_y)

        # Move horizontally and resolve collisions
        self.x += self.velocity_x
        self.rect.x = int(self.x)
        from systems.collision import resolve_horizontal_collision
        resolve_horizontal_collision(self, platforms)
        self.x = float(self.rect.x)

        # Move vertically and resolve collisions
        self.y += self.velocity_y
        self.rect.y = int(self.y)
        from systems.collision import resolve_vertical_collision
        resolve_vertical_collision(self, platforms)
        self.y = float(self.rect.y)

        # Update invulnerability
        if self.invulnerable_timer > 0:
            self.invulnerable_timer -= 1/60.0

        # Update animation state
        if self.velocity_y < 0:
            self.state = "jumping"
        elif self.velocity_y > 1.0 and not self.is_grounded:
            self.state = "falling"
        elif abs(self.velocity_x) > 0.5:
            self.state = "running"
        else:
            self.state = "idle"

        self.animation_timer += 0.05
        self.render_procedural_graphics()

    def jump(self, audio_manager):
        if self.is_grounded:
            self.velocity_y = PLAYER_JUMP_FORCE
            self.is_grounded = False
            audio_manager.play_jump()

    def take_damage(self, amount: int, audio_manager):
        if self.invulnerable_timer <= 0:
            from core.game_state import GameState
            # GameState handled in level / game coordinator
            self.invulnerable_timer = 1.5
            audio_manager.play_hurt()
            return True
        return False

    def render_procedural_graphics(self):
        self.image.fill((0, 0, 0, 0))
        color = COLOR_PLAYER_DMG if self.invulnerable_timer > 0 and int(self.animation_timer * 10) % 2 == 0 else COLOR_PLAYER

        # Body bounce / squash & stretch
        squash_x = 0
        squash_y = 0
        if self.state == "jumping":
            squash_y = -4
            squash_x = 4
        elif self.state == "running":
            squash_y = int(math.sin(self.animation_timer * 4) * 3)

        # Draw character body
        body_rect = pygame.Rect(4 - squash_x//2, 10 + squash_y, self.width - 8 + squash_x, self.height - 18 - squash_y)
        pygame.draw.rect(self.image, color, body_rect, border_radius=10)

        # Eyes
        eye_offset = 6 if self.facing_right else -6
        pygame.draw.circle(self.image, (255, 255, 255), (self.width // 2 + eye_offset, 22), 5)
        pygame.draw.circle(self.image, (20, 30, 50), (self.width // 2 + eye_offset + (2 if self.facing_right else -2), 22), 2)

        # Scarf / detail
        pygame.draw.rect(self.image, (240, 100, 80), (6, 28, self.width - 12, 6), border_radius=3)