"""
systems/collision.py - AABB collision detection and separation routines.
"""

import pygame

def check_collision(rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
    return rect1.colliderect(rect2)

def resolve_horizontal_collision(player, platforms):
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if player.velocity_x > 0:  # Moving right
                player.rect.right = platform.rect.left
            elif player.velocity_x < 0:  # Moving left
                player.rect.left = platform.rect.right

def resolve_vertical_collision(player, platforms):
    player.is_grounded = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            if player.velocity_y > 0:  # Falling down
                player.rect.bottom = platform.rect.top
                player.velocity_y = 0
                player.is_grounded = True
                if hasattr(platform, 'is_disappearing') and platform.is_disappearing:
                    platform.trigger_disappear()
            elif player.velocity_y < 0:  # Jumping up
                player.rect.top = platform.rect.bottom
                player.velocity_y = 0