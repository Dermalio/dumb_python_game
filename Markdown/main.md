```
from character import *
from mechanics import *
from world import *
from inventory import *
from characters_db import *

previous_room = starting_room
current_room = starting_room
player = spawn_characters("player")
goblin = spawn_characters("goblin_scout")

while True:
    print("=========================================================")
    print(f"You are in a {current_room.name}.")
    if current_room.enemies:
        print("---------------------------------------------------------")
        print(f"You've encountered an enemy: {current_room.enemies[0].name}!")
    print("=========================================================")

    action = choose_action(player, current_room, previous_room)

    if not action:
        break

    previous_room = current_room
    current_room = action


```


