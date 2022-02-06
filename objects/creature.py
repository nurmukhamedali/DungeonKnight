from .abstract import AbstractObject


class Creature(AbstractObject):
    """
        stats: options[
            endurance,
            strength,
            agility,
            luck,
            intelligence,
            charisma,
            perception
        ]

    """
    def __init__(self, icon, stats, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.calc_max_HP()
        self.hp = self.max_hp

    def calc_max_HP(self):
        self.max_hp = 5 + self.stats["endurance"] * 2

