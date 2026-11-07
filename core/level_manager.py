"""
core/level_manager.py - Level manager coordinating loading and transitions between 10 levels.
"""

from levels.level_01 import Level01
from levels.level_02 import Level02
from levels.level_03 import Level03
from levels.level_04 import Level04
from levels.level_05 import Level05
from levels.level_06 import Level06
from levels.level_07 import Level07
from levels.level_08 import Level08
from levels.level_09 import Level09
from levels.level_10 import Level10

class LevelManager:
    def __init__(self):
        self.levels = {
            1: Level01,
            2: Level02,
            3: Level03,
            4: Level04,
            5: Level05,
            6: Level06,
            7: Level07,
            8: Level08,
            9: Level09,
            10: Level10
        }

    def load_level(self, level_num: int):
        if level_num in self.levels:
            return self.levels[level_num]()
        return None