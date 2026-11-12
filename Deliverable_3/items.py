#Task 3


from dice import Dice


class Weapon:
    """Represents a weapon that deals damage based on a dice roll"""
 
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon
 
        Args:
            name (str): The name of the weapon.
            damage_dice (Dice): The dice used to calculate damage.
        """
        self.name = name
        self.damage_dice = damage_dice
 
    def roll_damage(self) -> int:
        """Roll the weapon's damage dice and return the damage"""
        return self.damage_dice.roll()
 
    def __repr__(self) -> str:
        """Representation of weapon object"""
        return f"Weapon(name={self.name}, damage_dice={self.damage_dice})"