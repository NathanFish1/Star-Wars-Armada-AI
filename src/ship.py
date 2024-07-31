def mm_to_pixel(mm):
    return mm * (130 / 25.4)


class Ship:
    def __init__(self, points, hull_points, fighter_defence, hull_zones, tokens, upgrade_slots, stat_line, move_set,
                 size, move_dials):
        self.move_dials = move_dials
        self.size = size
        self.move_set = move_set
        self.stat_line = stat_line
        self.upgrade_slots = upgrade_slots
        self.tokens = tokens
        self.hull_zones = hull_zones
        self.fighter_defence = fighter_defence
        self.hull_points = hull_points
        self.points = points

    def get_length(self):
        return mm_to_pixel(self.size.value[1])

    def get_width(self):
        return mm_to_pixel(self.size.value[0])

    def draw(self):
        pass

    def move(self):
        pass

    def actions(self):
        pass
