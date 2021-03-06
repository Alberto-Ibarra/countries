from classes.character import Character
from classes.ninja import Ninja
from classes.pirate import Pirate
import random

class Game:
    def __init__(self, score=0)
        self.score = score
        self.player1 = Ninja("Michelangelo")
        self.player2 = Pirate("Jack Sparrow")

    def battle(self):
        print("begin the battle")
        self.player2.attack(self.player1)
        self.player1.show_stats()
        self.player1.attack(self.player2)
        self.player2.show_stats()
        is_winner = False
        while not is_winner:
            if self.player1.health == 0 or self.player2.health == 0:
                is_winner = True
            p1_rand = random.randint(1,100)
            p2_rand = random.randint(1,100)

            self.player2.health -= round(self.player1.strength * (1 / p1_rand))
            self.player1.health -= round(self.player2.strength * (1 / p2_rand))

            print(f"{self.player1}: {self.player1.health}, {self.player2}: {self.player2.health}")

if __name__ == "__main__":
    game = Game()
    game.battle()

    