from game_simulator_v2 import Character

class Battle:

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
        """Simulate a single round of battle where the hero attacks the enemy and vice versa"""
        if self.hero.is_alive and self.enemy.is_alive:
            self.hero.attack(self.enemy)
            if self.enemy.is_alive:  # Enemy only attacks if still alive
                self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is defeated"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
            print(f"{self.hero.name} HP: {self.hero.hp}, {self.enemy.name} HP: {self.enemy.hp}")

        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")

