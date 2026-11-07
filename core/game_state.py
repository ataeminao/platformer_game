"""
core/game_state.py - Persistent game state container for score, lives, progress, and settings.
"""

class GameState:
    def __init__(self):
        self.reset_game()
        self.unlocked_level = 1
        self.sound_enabled = True

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.health = 100
        self.max_health = 100
        self.current_level = 1
        self.collectibles_collected = 0
        self.total_collectibles = 0
        self.level_time = 0.0

    def reset_level_stats(self):
        self.collectibles_collected = 0
        self.level_time = 0.0