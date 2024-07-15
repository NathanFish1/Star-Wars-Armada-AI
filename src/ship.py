from src import Unit


class Ship(Unit):
    def __init__(self, health, shield, size):
        self.health = health
        self.shield = shield
        self.size = size

    @property
    def health(self):
        return self.health

    @property
    def shield(self):
        return self.shield

    @property
    def size(self):
        return self.size

    def draw(self):
        pass

    def move(self):
        pass

    def actions(self):
        pass
