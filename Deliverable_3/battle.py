"""Turn-based combat between two characters (Task 5)."""

from game_simulator_v2 import Character


class Battle:
    """Manages turn-based combat between a hero and an enemy"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the Battle

        Args:
            hero (Character): The hero character.
            enemy (Character): The enemy character.
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round: the hero attacks, then the enemy if still alive"""
        if self.hero.is_alive and self.enemy.is_alive:
            self.hero.attack(self.enemy)
            if self.enemy.is_alive:  # Enemy only attacks if still alive
                self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
            print(f"{self.hero.name} HP: {self.hero.hp}, "
                  f"{self.enemy.name} HP: {self.enemy.hp}")

        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")

    def __repr__(self) -> str:
        """Representation of battle object"""
        return f"Battle(hero={self.hero!r}, enemy={self.enemy!r})"
