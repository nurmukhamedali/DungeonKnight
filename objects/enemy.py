from .interactive import Interactive
from .creature import Creature


class Enemy(Creature, Interactive):
    def __init__(self, icon, stats, xp, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.hp = xp

    def interact(self, engine, hero):
        # TODO how hero will interact with his enemy

        pass

