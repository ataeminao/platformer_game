"""
systems/scoring.py - Scoring system and bonus calculations.
"""

class ScoringSystem:
    @staticmethod
    def calculate_completion_bonus(time_taken: float, collectibles: int) -> int:
        time_bonus = max(0, int(1000 - time_taken * 10))
        collectible_bonus = collectibles * 100
        return time_bonus + collectible_bonus