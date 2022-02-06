from . import Effect


class Berserk(Effect):
    """
    Berserk - effect:

        -3 points perception,
        -3 points charisma,
        -3 points intelligence,

        +7 points endurance,
        +7 points strength,
        +7 points agility,
        +7 points luck


    """
    def apply_effect(self):
        increase_keys = ['strength', 'endurance', 'agility', 'luck']
        decrease_keys = ['perception', 'charisma', 'intelligence']

        for key in increase_keys:
            self.stats[key] += 7
        for key in decrease_keys:
            self.stats[key] -= 3
        self.stats["HP"] += 50
        return self.stats.copy()

