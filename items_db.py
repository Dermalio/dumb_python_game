CONSUMABLES ={
    "minor_health_potion" : {
        "name": "Minor Health Potion",
        "effect_magnitude": 30,
        "duration": 1,
        "stat": "health",
        "difficulty": range(1, 5),
        "drop_chance": 0.35,
        "use_message": "You chug {name}. {magnitude} {stat} restored!",
    },
    "health_potion" : {
        "name": "Health Potion",
        "effect_magnitude": 50,
        "duration": 1,
        "stat": "health",
        "difficulty": range(4, 11),
        "drop_chance": 0.3,
        "use_message": "You chug {name}. {magnitude} {stat} restored!",
    },
    "greater_health_potion" : {
        "name": "Greater Health Potion",
        "effect_magnitude": 90,
        "duration": 1,
        "stat": "health",
        "difficulty": range(9, 14),
        "drop_chance": 0.25,
        "use_message": "You chug {name}. {magnitude} {stat} restored!",
    },
    "minor_mana_potion" : {
        "name": "Minor Mana Potion",
        "effect_magnitude": 30,
        "duration": 1,
        "stat": "mana",
        "difficulty": range(1, 5),
        "drop_chance": 0.35,
        "use_message": "You chug {name}. {magnitude} {stat} restored!",
    },
    "mana_potion" : {
        "name": "Mana Potion",
        "effect_magnitude": 50,
        "duration": 1,
        "stat": "mana",
        "difficulty": range(4, 11),
        "drop_chance": 0.3,
        "use_message": "You chug {name}. {magnitude} {stat} restored!",
    },
    "greater_mana_potion" : {
        "name": "Greater Mana Potion",
        "effect_magnitude": 90,
        "duration": 1,
        "stat": "mana",
        "difficulty": range(9, 14),
        "drop_chance": 0.25,
        "use_message": "You chug {name}. {magnitude} {stat} restored!",
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
        "stat": "health",
        "difficulty": range(1, 14),
        "drop_chance": 0.2,
        "use_message": "You used {name}. Enemy's {stat} reduced by {magnitude}!",
    },
    "searing_decay": {
        "name": "Searing Decay",
        "effect_magnitude": 9,
        "duration": 5,
        "stat": "health",
        "difficulty": range(1, 14),
        "drop_chance": 0.15,
        "use_message": "You used {name}. Enemy's {stat} reduced by {magnitude}!",
    }
}
