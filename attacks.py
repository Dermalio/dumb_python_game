import random

class Attack:
    def __init__(self, name, damage_modifier, hit_threshold, attack_count):
        self.name = name
        self.damage_modifier = damage_modifier
        self.hit_threshold = hit_threshold
        self.attack_count = attack_count
        self.accuracy_modifier = 1

    def __repr__(self):
        return self.name

    def execute_attack(self, attacker, target):
        base_damage = (attacker.attack_power * self.damage_modifier) - target.resistance
        final_damage = int(max(0, base_damage))
        for hit in range(self.attack_count):
            hit_chance = random.random()
            total_accuracy = self.hit_threshold * self.accuracy_modifier
            if hit_chance <= total_accuracy:
                crit_chance = random.random()
                if crit_chance <= attacker.crit_chance:
                    target.health -= int(final_damage * 1.5)
                    print(f"Critical hit! {attacker.name} dealt {int(final_damage * 1.5)}. {target.name} has {target.health} HP left.")
                else:
                    target.health -= final_damage
                    print(f"{attacker.name} dealt {final_damage} damage. {target.name} has {target.health} HP left.")
            else:
                print("Attack missed!")


class LightAttack(Attack):
    def __init__(self):
        super().__init__(
            name="Light Attack",
            damage_modifier=1,
            hit_threshold=0.8,
            attack_count=1)

class HeavyAttack(Attack):
    def __init__(self):
        super().__init__(
            name="Heavy Attack",
            damage_modifier=2,
            hit_threshold=0.6,
            attack_count=1)

class Jab(Attack):
    def __init__(self):
        super().__init__(
            name="Jab",
            damage_modifier=0.6,
            hit_threshold=1,
            attack_count=1)
