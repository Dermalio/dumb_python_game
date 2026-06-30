```
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def use(self, target):
        raise NotImplementedError(f"Error: {self.name} is missing a use() method!")

class Consumable(Item):
    def __init__(self, name, effect_magnitude, stat_to_affect, use_message):
        super().__init__(name)
        self.effect_magnitude = effect_magnitude
        self.stat_to_affect = stat_to_affect
        self.use_message = use_message

    def use(self, target):
        if hasattr(target, self.stat_to_affect):
            max_stat = getattr(target, "max_" + self.stat_to_affect, None)
            stat = getattr(target, self.stat_to_affect)
            stat += self.effect_magnitude
            if max_stat:
                setattr(target, self.stat_to_affect, min(max_stat, stat))
            else:
                setattr(target, self.stat_to_affect, stat)
            print(self.use_message.format(
                name=self.name,
                magnitude=self.effect_magnitude,
                stat=self.stat_to_affect
            ))
        else:
            print("No stats to affect")
        return True

class Throwable(Item):
    def __init__(self, name, effect_magnitude, stat_to_affect, use_message, duration):
        super().__init__(name)
        self.effect_magnitude = effect_magnitude
        self.stat_to_affect = stat_to_affect
        self.use_message = use_message
        self.duration = duration

    def use(self, target):
        if hasattr(target, self.stat_to_affect):
            stat = getattr(target, self.stat_to_affect)
            stat -= self.effect_magnitude
            setattr(target, self.stat_to_affect, max(0, stat))
            print(self.use_message.format(
                name=self.name,
                magnitude=self.effect_magnitude,
                stat=self.stat_to_affect
            ))
        else:
            print("No stats to affect")
        return True
        
```