class GameCharacter:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("'name' must be a string.")
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name  # solo lectura

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if not isinstance(new_health, (int, float)):
            raise TypeError("'health' must be a number.")
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if not isinstance(new_mana, (int, float)):
            raise TypeError("'mana' must be a number.")
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100   # usa el setter
        self.mana = 50      # usa el setter
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Mana: {self.mana}")
