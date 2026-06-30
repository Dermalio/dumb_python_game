import random
from rooms_db import *
from config import *


class Exploration:
    def __init__(self):
        self.rooms = [starting_room]
        self.spawn_chance = BASE_SPAWN_CHANCE
        self.rooms_cleared = 0

    def push(self, room):
        self.rooms.append(room)

    def size(self):
        return len(self.rooms)

    def peek(self):
        if len(self.rooms) == 0:
            return None
        return self.rooms[-1]

    def pop(self):
        if len(self.rooms) == 0:
            return None
        room = self.rooms[-1]
        del self.rooms[-1]
        return room

    def reset_spawn_chance(self):
        self.spawn_chance = BASE_SPAWN_CHANCE

class Room:
    def __init__(self):
        self.name = f"{random.choice(ROOM_ADJECTIVES)} {random.choice(ROOM_TYPES)}"
        self.enemies = []

    def __repr__(self):
        return self.name

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

starting_room = Room()
starting_room.name = "Cell"