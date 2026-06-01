```
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Potion(Item):
    def __init__(self, name, effect_magnitude):
        super().__init__(name)
        self.effect_magnitude = effect_magnitude
    def use(self, target):
        raise NotImplementedError(f"Error: {self.name} is missing a consume() method!")

class HealthPotion(Potion):
    def __init__(self, name, effect_magnitude):
        super().__init__(name, effect_magnitude)

    def use(self, target):
        missing_health = target.max_health - target.health
        actual_heal = min(self.effect_magnitude, missing_health)
        target.health += actual_heal
        print(f"You drank the {self.name}. Recovered {actual_heal} HP. ({target.health}/{target.max_health})")
        return True ## To check if the item is one use or reusable. T - single use F - reusable

class ManaPotion(Potion):
    def __init__(self, name, effect_magnitude):
        super().__init__(name, effect_magnitude)

    def use(self, target):
        missing_mana = target.max_mana - target.mana
        actual_regen = min(self.effect_magnitude, missing_mana)
        target.mana += actual_regen
        print(f"You drank the {self.name}. Recovered {actual_regen} mana. ({target.mana}/{target.max_mana})")
        return True
```