CONSUMABLES ={
    "minor_health_potion" : {
        "name": "Minor Health Potion",
        "effect_magnitude": 30,
        "difficulty": range(1, 5),
        "drop_chance": 0.35,
    },
    "health_potion" : {
        "name": "Health Potion",
        "effect_magnitude": 50,
        "difficulty": range(4, 11),
        "drop_chance": 0.3,
    },
    "greater_health_potion" : {
        "name": "Greater Health Potion",
        "effect_magnitude": 90,
        "difficulty": range(9, 14),
        "drop_chance": 0.25,
    },
    "minor_mana_potion" : {
        "name": "Minor Mana Potion",
        "effect_magnitude": 30,
        "difficulty": range(1, 5),
        "drop_chance": 0.35,
    },
    "mana_potion" : {
        "name": "Mana Potion",
        "effect_magnitude": 50,
        "difficulty": range(4, 11),
        "drop_chance": 0.3,
    },
    "greater_mana_potion" : {
        "name": "Greater Mana Potion",
        "effect_magnitude": 90,
        "difficulty": range(9, 14),
        "drop_chance": 0.25,
    }

}

BUFFS = {
    "warriors_wrath": {
        "name": "Warrior's Wrath",
        "effect_magnitude": 10,
        "stat": "attack_power",
        "difficulty": range(1, 14),
        "drop_chance": 0.1,
    },
    "sages_wisdom": {
        "name": "Sage's Wisdom",
        "effect_magnitude": 30,
        "stat": "max_mana",
        "difficulty": range(1, 14),
        "drop_chance": 0.1, #TODO: MAKE CLASSES USING MANA AS A RESOURCE FOR ATTACKS
    },
    "chitin_armor": {
        "name": "Chitin Armor",
        "effect_magnitude": 10,
        "stat": "resistance",
        "difficulty": range(1, 14),
        "drop_chance": 0.1,
    }

}

THROWABLE = {
    "fire_flask": {
        "name": "Fire Flask",
        "effect_magnitude": 30,
        "duration": 1,
        "difficulty": range(1, 14),
        "drop_chance": 0.2,
    },
    "searing_decay": {
        "name": "Searing Decay",
        "effect_magnitude": 9,
        "duration": 5,
        "difficulty": range(1, 14),
        "drop_chance": 0.15,
    }
}
