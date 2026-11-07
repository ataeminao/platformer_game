"""
systems/save_system.py - JSON-based progress persistence.
"""

import json
import os

class SaveSystem:
    SAVE_FILE = "save_game.json"

    @classmethod
    def save_progress(cls, unlocked_level: int, high_score: int):
        data = {
            "unlocked_level": unlocked_level,
            "high_score": high_score
        }
        try:
            with open(cls.SAVE_FILE, 'w') as f:
                json.dump(data, f)
        except Exception:
            pass

    @classmethod
    def load_progress(cls) -> dict:
        if not os.path.exists(cls.SAVE_FILE):
            return {"unlocked_level": 1, "high_score": 0}
        try:
            with open(cls.SAVE_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {"unlocked_level": 1, "high_score": 0}