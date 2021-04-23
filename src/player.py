class Player:
    def __init__(self, name, power, void, wells, army):
        self.name = name
        self.power = power
        self.void = void
        self.wells = wells
        self.army = army

    def well_gps(self):
        return self.wells / 2.0

    def void_gps(self):
        return self.void / 100.0

    def total_gps(self):
        return self.well_gps() + self.void_gps()
