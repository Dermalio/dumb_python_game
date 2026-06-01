import re


class Character:
    def __init__(self, name, attack_power, max_health, resistance, crit_chance):
        self.name = name
        self.attack_power = attack_power
        self.max_health = max_health
        self.health = self.max_health
        self.resistance = resistance
        self.inventory = []
        self.crit_chance = crit_chance
        self.attacks = []

    def __repr__(self):
        return self.name

    def pick_up_item(self, item):
        self.inventory.append(item)
        if re.search("[aeio]", item.name[0]):
            print(f"{self.name} picked up an {item}.")
        else:
            print(f"{self.name} picked up a {item}.")

    def use_item(self, searched_item):
        is_spent = searched_item.use(self)
        if is_spent:
            self.inventory.remove(searched_item)
        return


    def show_stats(self):
        print("\n" + "=" * 20)
        print(f" STATUS: {self.name.upper()} ")
        print("=" * 20)
        print(f" HP:     {self.health}/{self.max_health}")
        print(f" ATK:    {self.attack_power}")
        print(f" DEF:    {self.resistance}")
        print("=" * 20 + "\n")



