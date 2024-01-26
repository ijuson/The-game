import random

class Building:
    def __init__(self, name, build_time, attack_power):
        self.name = name
        self.build_time = build_time
        self.attack_power = attack_power

class ClashOfClans:
    def __init__(self):
        self.buildings = [
            Building("Wall", 5, 5),
            Building("Barracks", 10, 10),
            Building("Cannon", 15, 15),
            Building("Magic Tower", 20, 20),
        ]
        self.village = {}
        self.opponent_village = {}

    def train(self, building_name):
        building = self.get_building(building_name)
        self.village[building_name] = 0
        self.train_units(building_name)

    def get_building(self, building_name):
        for building in self.buildings:
            if building.name == building_name:
                return building
        return None

    def train_units(self, building_name):
        units = random.randint(1, 10)
        self.village[building_name] += units

    def attack(self):
        total_attack_power = 0
        for building_name, units in self.village.items():
            building = self.get_building(building_name)
            total_attack_power += units * building.attack_power
        self.opponent_village["HP"] -= total_attack_power

    def show_village(self):
        print("Village:")
        for building_name, units in self.village.items():
            print(f"{building_name}: {units}")
        print(f"Opponent's HP: {self.opponent_village['HP']}")

def main():
    game = ClashOfClans()
    while True:
        print("\nOptions:")
        print("1. Train units")
        print("2. Attack")
        print("3. Show village")
        print("4. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            building_name = input("Enter building name: ")
            game.train(building_name)
        elif option == 2:
            game.attack()
        elif option == 3:
            game.show_village()
        elif option == 4:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()