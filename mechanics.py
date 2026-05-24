from curses.ascii import isdigit
import random
import world


def inventory_menu(player):
    print("Your inventory:")
    enumerated_inventory = list(enumerate(player.inventory, 1))
    print("0: <- Go back")
    for i in enumerated_inventory:
        print(f"{i[0]}: {i[1]}")
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
                    player.attack(enemy)
                    players_turn_spent = True
                case '2':
                    if inventory_menu(player):
                        players_turn_spent = True
                case '3':
                    player.show_stats()
                case '4':
                    escape_chance = random.random()
                    if escape_chance < 0.75:
                        return "ran"
                    else:
                        print("Escape failed")
                        players_turn_spent = True
        if enemy.health > 0:
            enemy.attack(player)
        else:
            return "won"
        if player.health <= 0:
            return "lost"

def choose_direction(chosen_room):
    while True:
        move_command = input("Choose a direction to go (north, south, east, west): ").lower()

        if move_command in chosen_room.exits.keys():
            current_room = chosen_room.exits[move_command]
            print(f"You entered {current_room.name}")
            return current_room
        else:
            print("You bump into a wall, choose a different direction")


def choose_action(player, current_room, previous_room):
    while True:
        action_input = input("What do you want to do? \n"
                             "1. Move\n"
                             "2. Attack\n"
                             "3. Use\n"
                             "4. Stat check\n").lower()

        if action_input == "1" or action_input == "move": # TODO: match case could do well here too like in battle()
            current_room = choose_direction(current_room)  # TODO: can't move before defeating all enemies
            return current_room
        elif action_input == "2" or action_input == "attack":
            print(current_room.enemies[0].name) ## TODO: Make it show at the entrance
            if current_room.enemies:
                battle_outcome = battle(player, current_room.enemies[0])
                match battle_outcome:
                    case "won":
                        print("You won!")
                        current_room.enemies.remove(current_room.enemies[0])
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
