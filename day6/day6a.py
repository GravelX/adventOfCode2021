import os

class LanterFish():
    def __init__(self, dbr):
        self.dbr = dbr # (days before reproduction)

    def reproduce(self):
        if (self.dbr < 0):
            self.dbr = 6
            return LanterFish(8)
        else:
            return None

    def get_older(self):
        self.dbr -= 1

class Simulation():
    def __init__(self):
        self.current_day = 0
        self.fishies = []
        self.load_fishies()

    def load_fishies(self):
        file_path = os.path.join(os.path.dirname(__file__), "input.txt")

        with open(file_path) as f:
            data = f.readline()

        dbrs = data.split(",")

        fishies = []
        for value in dbrs:
            fishies.append(LanterFish(int(value)))

        self.fishies = fishies
        self.print_status()

    def tick(self):
        new_borns = []
        for fish in self.fishies:
            fish.get_older()
            new_fish = fish.reproduce()
            if new_fish is not None:
                new_borns.append(new_fish)

        self.fishies.extend(new_borns)
        self.current_day += 1
        self.print_status()

    def print_status(self):
        print("Day {}: There are currently {} lantern fish in the sea!".format(self.current_day, len(self.fishies)))

## MAIN ##
days_of_simulation = 80
fish_simulation = Simulation()
for i in range(0, days_of_simulation):
    fish_simulation.tick()
        