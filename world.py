class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.enemies = []

    def __repr__(self):
        return self.name

    def add_exit(self, direction, neighbor_room):
        direction_pairs = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
        }

        self.exits[direction] = neighbor_room
        reverse_direction = direction_pairs[direction]
        neighbor_room.exits[reverse_direction] = self

    def add_enemy(self, enemy):
        self.enemies.append(enemy)
