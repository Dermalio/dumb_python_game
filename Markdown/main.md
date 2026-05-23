```
from character import *
from mechanics import *
from world import *
from inventory import *

cell = Room("Cell", "A damp, dark starting room.")
hallway = Room("Hallway", "A long corridor with flickering torches.")
cell.add_exit("north", hallway)
previous_room = None
current_room = cell
player = Player("Bodzio", 60, 370, 40)
goblin = Goblin("Goblin", 50, 350, 30)
health_potion = HealthPotion("Minor Health Potion", 30)
player.pick_up_item(health_potion)
hallway.add_enemy(goblin)

while True:
    print(f"You are in a {current_room.name}.")
    print(f"About this this place: {current_room.description}")
    print(f"Places you can go to: {current_room.exits}")

    action = choose_action(player, current_room, previous_room)

    if not action:
        break

    previous_room = current_room
    current_room = action
```


