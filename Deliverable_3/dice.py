"""Dice with any number of sides for random damage (Task 2)."""

import random


class Dice:
    """Represents an n-sided dice (n >= 2)"""

    def __init__(self, sides: int = 6) -> None:
        """Initialise the Dice with a number of sides (default = 6)"""
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a number between 1 and sides"""
        return random.randint(1, self.sides)

    def __call__(self) -> int:
        """Allow the Dice object to be called like a function to roll it"""
        return self.roll()

    def __repr__(self) -> str:
        """Return a string representation of the Dice object"""
        return f"Dice(sides={self.sides})"
