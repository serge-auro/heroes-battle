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
        print(f"The Fighter: {self.name}; str {self.strength}; dex {self.dexterity}; int {self.intelligence}"
              f"; health {self.health}; weapon {weapon}")


class Monster(Actor):
    def __init__(self, name, strength, dexterity, intelligence, health):
        super().__init__(name, strength, dexterity, intelligence, health)

    def take_damage(self, damage):
        physic = damage["physic"] - self.strength / STAT_MODIFIER
        mental = damage["mental"] - self.intelligence / STAT_MODIFIER
        if physic > 0:
            self.health -= physic
        if mental > 0:
            self.health -= mental
        if self.health <= 0:
            print(f"{self.name} died. You've won!")
        else:
            print(f"Monster health is {self.health}.")

    def print_all(self):
        print(f"The Monster: {self.name}; str {self.strength}; dex {self.dexterity}; int {self.intelligence}"
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


# MAIN #
fighter1 = Fighter("The I", 30, 25, 10, 100)
fighter1.print_all()

weapon1 = Sword("Sword", 50, 0)
weapon2 = Bow("Bow", 50, 0)
weapon3 = Staff("Staff", 0, 75)

fighter1.change_weapon(weapon1)
monster1 = Monster("Magic boll", 30, 25, 50, 100)
monster1.print_all()

damage = fighter1.weapon.attack(fighter1.strength, fighter1.dexterity, fighter1.intelligence)
print(f"Fighter generates {damage} damage.")
monster1.take_damage(damage)

monster2 = Monster("Bear", 50, 5, 0, 1000)
monster2.print_all()

fighter1.change_weapon(weapon2)
damage = fighter1.weapon.attack(fighter1.strength, fighter1.dexterity, fighter1.intelligence)
print(f"Fighter generates {damage} damage.")
monster2.take_damage(damage)

fighter1.change_weapon(weapon3)
damage = fighter1.weapon.attack(fighter1.strength, fighter1.dexterity, fighter1.intelligence)
print(f"Fighter generates {damage} damage.")
monster2.take_damage(damage)

fighter1.change_weapon(weapon1)
damage = fighter1.weapon.attack(fighter1.strength, fighter1.dexterity, fighter1.intelligence)
print(f"Fighter generates {damage} damage.")
monster2.take_damage(damage)

