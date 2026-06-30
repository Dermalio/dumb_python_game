from inventory import Consumable
from world import *
from characters_db import CHARACTERS
from character import Character
from attacks import *
from items_db import *
from config import *

dungeon_manager_stack = Exploration()


def inventory_menu(player):
    print("Your inventory:")
    enumerated_inventory = list(enumerate(player.inventory, 1))
    print("0: <- Go back")
    for i in enumerated_inventory:
        print(f"{i[0]}: {i[1].name}")
    inventory_input = input("Which item do you want to use? ")
    if "back" in inventory_input or inventory_input == "0":
        return False
    elif inventory_input.isdigit():
        inventory_input = int(inventory_input)
        if 0 < inventory_input <= len(player.inventory):
            player.use_item(player.inventory[inventory_input - 1])
            return True
        else:
            print("No such item in your inventory")
            return False
    else:
        print("Invalid input, choose a number")
        return False

def skills_menu(player, target):
    print("Your attacks:")
    enumerated_attacks = list(enumerate(player.attacks, 1))
    print("0: <- Go back")
    for i in enumerated_attacks:
        print(f"{i[0]}: {i[1]}")
    attack_input = input("How do you want to attack? ")
    if "back" in attack_input or attack_input == "0":
        return False
    elif attack_input.isdigit():
        attack_input = int(attack_input)
        if 0 < attack_input <= len(player.attacks):
            player.attacks[attack_input - 1].execute_attack(player, target)
            return True
        else:
            print("Invalid input, no such attack")
            return False
    else:
        print("Invalid input, choose a number")
        return False

def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        players_turn_spent = False
        while not players_turn_spent:
            fight_input = input('Choose an action: \n'
                                '1. Attack\n'
                                '2. Use item\n'
                                '3. Stat check\n'
                                '4. Run away\n').lower()
            match fight_input:
                case '1':
                    if skills_menu(player, enemy):
                        players_turn_spent = True
                case '2':
                    if inventory_menu(player):
                        players_turn_spent = True
                case '3':
                    player.show_stats()
                case '4':
                    escape_chance = random.random()
                    if escape_chance < FLEE_CHANCE:
                        return "ran"
                    else:
                        print("Escape failed")
                        players_turn_spent = True
        if enemy.health > 0:
            enemy.attacks[0].execute_attack(enemy, player)
        else:
            return "won"
        if player.health <= 0:
            return "lost"

def enemy_selection(room_count):
    temp_enemy_pool = []
    for enemy, stats in CHARACTERS.items():
        if room_count in stats["difficulty"]:
            temp_enemy_pool.append(enemy)
    return temp_enemy_pool

def choose_direction(player_location):
    while dungeon_manager_stack.rooms_cleared <= ROOMS_TO_WIN:
        move_command = input("How will you proceed?\n"
                             "1. Go deeper\n"
                             "2. Retreat\n").lower()
        spawn_risk = random.random()
        match move_command:
            case "1" | "deeper":
                if player_location == dungeon_manager_stack.peek():
                    current_room = Room()
                    dungeon_manager_stack.push(current_room)
                    if spawn_risk < dungeon_manager_stack.spawn_chance:
                        enemy_pool = enemy_selection(dungeon_manager_stack.rooms_cleared)
                        enemy = spawn_characters(random.choice(enemy_pool))
                        current_room.add_enemy(enemy)
                        dungeon_manager_stack.reset_spawn_chance()
                    else:
                        dungeon_manager_stack.spawn_chance += SPAWN_CHANCE_INCREASE
                        dungeon_manager_stack.rooms_cleared += 1
                    return current_room
                else:
                    return dungeon_manager_stack.peek()
            case "2" | "retreat":
                if dungeon_manager_stack.size() > 1:
                    dungeon_manager_stack.pop()
                    current_room = dungeon_manager_stack.peek()
                    print(f"You have retreated to {current_room.name}")
                    return current_room
                else:
                    print("You can't retreat any further!")
            case _:
                print("You bump into a wall, choose a different direction")
    print("You've reached the exit. Good luck on your next journey!")
    return None

def roll_category(category, room_count):
    filtered_items = []
    drop_chance_sum = 0
    roll = random.random()
    for item, stats in category.items():
        if room_count in stats["difficulty"]:
            filtered_items.append((item, stats))
            drop_chance_sum += stats["drop_chance"]
    if drop_chance_sum > 0 and roll <= MAX_DROP_THRESHOLD:
        for item in filtered_items:
            normalized_drop_chance = (item[1]["drop_chance"] / drop_chance_sum) * MAX_DROP_THRESHOLD
            if roll > normalized_drop_chance:
                roll -= normalized_drop_chance
            else:
                return item[0]
    return None

def generate_loot(room_count):
    loot = []
    consumable = roll_category(CONSUMABLES, room_count)
    if consumable:
        loot.append(consumable)

    buff = roll_category(BUFFS, room_count)
    if buff:
        loot.append(buff)

    throwable = roll_category(THROWABLE, room_count)
    if throwable:
        loot.append(throwable)

    return loot

def distribute_loot(player, loot_list):
    for item in loot_list:
        if item in CONSUMABLES:
            item_scheme = CONSUMABLES[item]
            new_item = Consumable(
                item_scheme["name"],
                item_scheme["effect_magnitude"],
                item_scheme["stat"],
                item_scheme["use_message"])
            player.pick_up_item(new_item)
        elif item in THROWABLE:
            item_scheme = THROWABLE[item]
            new_item = Consumable(
                item_scheme["name"],
                item_scheme["effect_magnitude"],
                item_scheme["stat"],
                item_scheme["use_message"])
            player.pick_up_item(new_item)
        elif item in BUFFS:
            item_scheme = BUFFS[item]
            buff_name = item_scheme["name"]
            magnitude = item_scheme["effect_magnitude"]
            stat = item_scheme["stat"]
            current_stat_value = getattr(player, stat)
            new_stat_value = current_stat_value + magnitude
            setattr(player, stat, new_stat_value)
            print(f"You used {buff_name}. {stat} permanently increased by {magnitude}.")



def choose_action(player, current_room, previous_room):
    while True:
        action_input = input("What do you want to do? \n"
                             "1. Move\n"
                             "2. Fight enemies\n"
                             "3. Use\n"
                             "4. Stat check\n").lower()

        if action_input == "1" or action_input == "move":
            if not current_room.enemies:
                current_room = choose_direction(current_room)
                return current_room
            print("You must defeat all enemies before moving.")
        elif action_input == "2" or action_input == "attack":
            if current_room.enemies:
                battle_outcome = battle(player, current_room.enemies[0])
                match battle_outcome:
                    case "won":
                        print("You won!")
                        current_room.enemies.remove(current_room.enemies[0])
                        dungeon_manager_stack.rooms_cleared += 1
                        loot = generate_loot(dungeon_manager_stack.rooms_cleared)
                        distribute_loot(player, loot)
                        return current_room
                    case "lost":
                        print("You lost! Game Over!")
                        return False
                    case "ran":
                        print(f"You escaped the fight! You've returned to the {previous_room.name}.")
                        return previous_room
            else:
                print("No enemies in sight, choose a different action")
        elif action_input == "3" or action_input == "use":
            inventory_menu(player)

        elif action_input == "4" or action_input == "stat":
            player.show_stats()

        else:
            print("No such action")

def spawn_characters(character_key):
    attack_mapping = {
        "Light Attack": LightAttack,
        "Heavy Attack": HeavyAttack,
        "Jab": Jab
    }

    if character_key in CHARACTERS:
        character_stats = CHARACTERS[character_key]
        character = Character(character_stats["name"],
                  character_stats["attack_power"],
                  character_stats["max_health"],
                  character_stats["resistance"],
                  character_stats["crit_chance"])
        character.attacks = []
        for attack in character_stats["attacks"]:
            character_attack = attack_mapping[attack]()
            character.attacks.append(character_attack)
        return character
    else:
        raise Exception(f"No {character_key} in your database.")