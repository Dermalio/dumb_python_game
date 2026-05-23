import re
import inventory

class Character:
    def __init__(self, name, attack_power, max_health, resistance):
        self.name = name
        self.attack_power = attack_power
        self.max_health = max_health
        self.health = self.max_health
        self.resistance = resistance
        self.inventory = []

    def __repr__(self):
        return self.name

    def pick_up_item(self, item):
        self.inventory.append(item)
        if re.search("[aeio]", item.name[0]):
            print(f"{self.name} picked up an {item}.")
        else:
            print(f"{self.name} picked up a {item}.")

    def use_item(self, searched_item):
        print(f"{searched_item.name} used.")
        if isinstance(searched_item, inventory.Potion):
            searched_item.consume(self)
            self.inventory.remove(searched_item)
            return

    def attack(self, target):
        if self.health > 0:
            if self.attack_power > target.resistance:
                damage = self.attack_power - target.resistance
                target.health -= damage
                if target.health <= 0:
                    target.health = 0
                    print(f"{target.name} died")
                else:
                    print(f"{self.name} dealt {damage} damage to {target.name}. {target.name} has {target.health} hit points left.")
            elif self.attack_power <= target.resistance:
                print(f"{self.name}'s attacks are ineffective! {target.name}'s resistance is too high!")

    def show_stats(self):
        print("\n" + "=" * 20)
        print(f" STATUS: {self.name.upper()} ")
        print("=" * 20)
        print(f" HP:     {self.health}/{self.max_health}")
        print(f" ATK:    {self.attack_power}")
        print(f" DEF:    {self.resistance}")
        print("=" * 20 + "\n")


class Player(Character):
    def __init__(self, name, attack_power, max_health, resistance):
        super().__init__(name, attack_power, max_health, resistance)

class Goblin(Character):
    def __init__(self, name, attack_power, max_health, resistance):
        super().__init__(name, attack_power, max_health, resistance)

