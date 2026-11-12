from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Base damage dealt when character attacks (default = 10)
            weapon (Weapon | None): Optional equipped weapon (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicates private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            dmg = self.weapon.roll_damage()
        else:
            dmg = self.damage
        target.take_damage(dmg)

    def take_damage(self, amount: int) -> None:
        """Reduce own HP by amount, but not below 0"""
        self._hp -= amount
        self._hp = max(self._hp, 0)  # HP cannot end up lower than 0

    def heal(self, amount: int) -> None:
        """Increase own HP by amount, but not above hp_max"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # HP cannot exceed hp_max

    def introduce(self) -> None:
        """Prints a string that introduces the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property: True if the character has HP left, otherwise False"""
        return self._hp > 0


class Warrior(Character):
    """A defensive specialist that reduces incoming damage with armor"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Initialise the Warrior

        Args:
            armor (int): Amount subtracted from incoming damage (default = 5)
            Other arguments as in Character.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce incoming damage by armor (never below 0) before applying it"""
        reduced = max(amount - self.armor, 0)
        super().take_damage(reduced)


class Mage(Character):
    """A resource-based attacker that spends mana on spell attacks"""

    SPELL_COST = 10
    MANA_RESTORE = 5

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, mana: int = 30,
                 mana_max: int = 30) -> None:
        """
        Initialise the Mage

        Args:
            mana (int): Current mana (default = 30)
            mana_max (int): Maximum mana (default = 30)
            Other arguments as in Character.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """
        Spell attack (double base damage, no weapon) if mana >= 10,
        otherwise a normal attack (with weapon if equipped) that restores 5 mana.
        """
        if self.mana >= self.SPELL_COST:
            self.mana -= self.SPELL_COST
            target.take_damage(2 * self.damage)
        else:
            super().attack(target)
            self.mana = min(self.mana + self.MANA_RESTORE, self.mana_max)