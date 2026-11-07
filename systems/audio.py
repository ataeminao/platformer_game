"""
systems/audio.py - Procedural sound synthesizer using Pygame mixer.
"""

import pygame
import numpy as np

class AudioManager:
    def __init__(self):
        self.enabled = True
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=1)
        except Exception:
            self.enabled = False

    def play_jump(self):
        if not self.enabled: return
        try:
            sample_rate = 22050
            duration = 0.15
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
            freq = np.linspace(200, 600, len(t))
            wave = 0.3 * np.sin(2 * np.pi * freq * t)
            sound = pygame.mixer.Sound(buffer=(wave * 32767).astype(np.int16))
            sound.set_volume(0.3)
            sound.play()
        except Exception:
            pass

    def play_coin(self):
        if not self.enabled: return
        try:
            sample_rate = 22050
            duration = 0.1
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
            wave = 0.3 * np.sin(2 * np.pi * 900 * t)
            sound = pygame.mixer.Sound(buffer=(wave * 32767).astype(np.int16))
            sound.set_volume(0.3)
            sound.play()
        except Exception:
            pass

    def play_hurt(self):
        if not self.enabled: return
        try:
            sample_rate = 22050
            duration = 0.2
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
            wave = 0.4 * np.sin(2 * np.pi * 120 * t) * np.exp(-t * 5)
            sound = pygame.mixer.Sound(buffer=(wave * 32767).astype(np.int16))
            sound.set_volume(0.4)
            sound.play()
        except Exception:
            pass

    def play_powerup(self):
        if not self.enabled: return
        try:
            sample_rate = 22050
            duration = 0.3
            t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
            freq = np.linspace(300, 900, len(t))
            wave = 0.3 * np.sin(2 * np.pi * freq * t)
            sound = pygame.mixer.Sound(buffer=(wave * 32767).astype(np.int16))
            sound.set_volume(0.3)
            sound.play()
        except Exception:
            pass