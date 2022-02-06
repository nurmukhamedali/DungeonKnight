from . import Effect


class Weakness(Effect):
    """
    Weakness - effect:

        -2 points perception,
        -2 points charisma,
        -2 points intelligence,
        -2 points endurance,
        -2 points strength,
        -2 points agility,
        -2 points luck

    """
    def apply_effect(self):
        decrease_keys = ['perception', 'charisma', 'intelligence', 'strength', 'endurance', 'agility', 'luck']

        for key in decrease_keys:
            self.stats[key] += 2

        return self.stats.copy()
