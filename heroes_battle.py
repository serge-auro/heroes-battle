import random as rnd

STAT_MODIFIER = 3


class Actor:
    def __init__(self, name, strength, dexterity, intelligence, health):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        physic = damage["physic"] - self.strength
        mental = damage["mental"] - self.intelligence
        if physic > 0:
            self.health -= physic
        if mental > 0:
            self.health -= mental


class Weapon:
    def __init__(self, name, physic, mental):
        self.name = name
        self.damage = {"physic": physic, "mental": mental}
        self.rate = {"strength": 0, "dexterity": 0, "intelligence": 0}

    def attack(self, strength, dexterity, intelligence):
        physic = (self.damage["physic"] * self.rate["strength"] * strength / STAT_MODIFIER +
                  self.damage["physic"] * self.rate["dexterity"] * dexterity / STAT_MODIFIER)
        mental = self.damage["mental"] * self.rate["intelligence"] * intelligence / STAT_MODIFIER
        return {"physic": physic, "mental": mental}

    def print(self):
        print(f"Weapon: {self.name} physic dmg: {self.damage['physic']} mental dmg: {self.damage['mental']}")


class Fighter(Actor):
    def __init__(self, name, strength, dexterity, intelligence, health):
        super().__init__(name, strength, dexterity, intelligence, health)
        self.weapon = None

    def change_weapon(self, weapon : Weapon):
        self.weapon = weapon
        print(f"{weapon.name} is chosen.")

    def print_all(self):
        weapon = "None"
        if self.weapon is not None:
            weapon = self.weapon.name
        print(f"The Fighter is {self.name}; str {self.strength}; dex {self.dexterity}; int {self.intelligence}"
              f"; health {self.health}; weapon {weapon}")

    def resting_health(self):
        print("You are resting health")
        self.health = 100


class Monster(Actor):
    def __init__(self, name, strength, dexterity, intelligence, health):
        super().__init__(name, strength, dexterity, intelligence, health)
        physic = (strength / STAT_MODIFIER +
                 dexterity / STAT_MODIFIER)
        mental = intelligence / STAT_MODIFIER
        self.damage = {"physic": physic, "mental": mental}

    def print_all(self):
        print(f"There is a Monster - {self.name}; str {self.strength}; dex {self.dexterity}; int {self.intelligence}"
              f"; health {self.health}")


class Sword(Weapon):
    def __init__(self, name, physic, mental):
        super().__init__(name, physic, mental)
        self.rate = {"strength": 1, "dexterity": 0.1, "intelligence": 0}


class Bow(Weapon):
    def __init__(self, name, physic, mental):
        super().__init__(name, physic, mental)
        self.rate = {"strength": 0.1, "dexterity": 1, "intelligence": 0}


class Staff(Weapon):
    def __init__(self, name, physic, mental):
        super().__init__(name, physic, mental)
        self.rate = {"strength": 0.1, "dexterity": 0, "intelligence": 1}


def battle(player, monster):
    while player.is_alive() and monster.is_alive():
        print(f"The {monster.name} is appearing. Prepare to fight!")

        print("Master, choose your weapon:")
        print(f"1. {weapon1.name} {weapon1.damage["physic"]} physic {weapon1.damage["mental"]} mental dmg"
              f"\n2. {weapon2.name} {weapon2.damage["physic"]} physic {weapon2.damage["mental"]} mental dmg"
              f"\n3. {weapon3.name} {weapon3.damage["physic"]} physic {weapon3.damage["mental"]} mental dmg")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.change_weapon(weapon1)
        elif choice == "2":
            player.change_weapon(weapon2)
        elif choice == "3":
            player.change_weapon(weapon3)
        else:
            print("Invalid choice. Please choose again.")
            continue

        damage = player.weapon.attack(player.strength, player.dexterity, player.intelligence)
        print(f"Fighter generates {damage} damage.")
        monster.take_damage(damage)

        if monster.is_alive():
            physic = rnd.randint(1, 20) * monster.damage["physic"]
            mental = rnd.randint(1, 20) * monster.damage["mental"]
            player.take_damage({"physic": physic, "mental": mental})
            print(f"{monster.name} attacks! You receive damage.")

    if player.is_alive():
        print("You defeated the monster!")
    else:
        print("Game over. You were defeated by the monster.")

# MAIN #
print("Welcome to the Heroes Battle!")
name = input("What is your name? ")
fighter1 = Fighter(name, rnd.randrange(10, 40), rnd.randrange(10, 40), rnd.randrange(10, 40), 100)
fighter1.print_all()

weapon1 = Sword("Sword", rnd.randrange(30, 60), rnd.randrange(0, 5))
weapon2 = Bow("Bow", rnd.randrange(30, 60), rnd.randrange(0, 5))
weapon3 = Staff("Staff", rnd.randrange(0, 5), rnd.randrange(50, 90))

monster1 = Monster("Magic boll", 30, 25, 50, 100)
monster2 = Monster("Bear", 50, 5, 0, 500)
monster3 = Monster("Dragon", 20, 20, 5, 1000)

battle(fighter1, monster1)
if fighter1.is_alive():
    fighter1.resting_health()
    battle(fighter1, monster2)
if fighter1.is_alive():
    fighter1.resting_health()
    battle(fighter1, monster3)

print("Thank you for playing!")
