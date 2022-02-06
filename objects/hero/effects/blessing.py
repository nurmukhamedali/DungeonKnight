from . import Effect


class Blessing(Effect):
    """
    Blessing - effect:

        +2 points perception,
        +2 points charisma,
        +2 points intelligence,
        +2 points endurance,
        +2 points strength,
        +2 points agility,
        +2 points luck

    """
    def apply_effect(self):
        increase_keys = ['perception', 'charisma', 'intelligence', 'strength', 'endurance', 'agility', 'luck']

        for key in increase_keys:
            self.stats[key] += 2

        return self.stats.copy()
