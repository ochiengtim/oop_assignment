#Base Class: Superhero
class Superhero:
    def __init__(self, name, alias, power, level, origin):
        self.name = name
        self.alias = alias
        self._power = power       # Encapsulated attribute
        self._level = level       # Encapsulated attribute
        self.origin = origin

    def introduce(self):
        print(f"I am {self.alias}, aka {self.name} from {self.origin}!")
    
    def use_power(self):
        print(f"{self.alias} uses their power: {self._power}!")

    def level_up(self):
        self._level += 1
        print(f"{self.alias} leveled up! Current level: {self._level}")

    # Encapsulation: Getters & Setters for _power and _level
    def get_power(self):
        return self._power

    def set_power(self, new_power):
        print(f"{self.alias}'s power has been changed from {self._power} to {new_power}")
        self._power = new_power

    def get_level(self):
        return self._level

    def set_level(self, new_level):
        if new_level >= self._level:
            print(f"{self.alias} now has level {new_level}")
            self._level = new_level
        else:
            print("Level can't be decreased!")

#Subclass: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, alias, power, level, origin, max_altitude):
        super().__init__(name, alias, power, level, origin)
        self.max_altitude = max_altitude

    def fly(self):
        print(f"{self.alias} takes off and soars up to {self.max_altitude} meters!")

    # Polymorphism: Override use_power
    def use_power(self):
        print(f"{self.alias} unleashes wind shockwaves while flying!")

#Subclass: SpeedsterHero
class SpeedsterHero(Superhero):
    def __init__(self, name, alias, power, level, origin, top_speed):
        super().__init__(name, alias, power, level, origin)
        self.top_speed = top_speed

    def dash(self):
        print(f"{self.alias} dashes at {self.top_speed} km/h leaving a blur!")

    # Polymorphism: Override use_power
    def use_power(self):
        print(f"{self.alias} accelerates time with lightning-fast reflexes!")

#Testing the setup
if __name__ == "__main__":
    hero1 = FlyingHero("Clark Kent", "Superman", "Flight", 99, "Krypton", 10000)
    hero2 = SpeedsterHero("Barry Allen", "The Flash", "Super Speed", 85, "Central City", 3000)

    hero1.introduce()
    hero1.fly()
    hero1.use_power()
    hero1.level_up()
    hero1.set_power("Laser Vision")

    print()

    hero2.introduce()
    hero2.dash()
    hero2.use_power()
    hero2.level_up()
    hero2.set_level(90)
    hero2.set_level(70)  # should not allow downgrade
