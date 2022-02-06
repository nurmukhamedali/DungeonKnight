from .abstract import AbstractObject
from .interactive import Interactive


class Ally(AbstractObject, Interactive):
    def __init__(self, icon, action, position):
        self.sprite = icon
        self.action = action
        self.position = position

    def interact(self, engine, hero):
        self.action(engine, hero)

