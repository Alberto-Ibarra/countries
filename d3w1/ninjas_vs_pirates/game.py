from classes.ninja import Ninja
from classes.pirate import Pirate

import random
print(random.randint(0,10))

class Game:
    def __init__(self, score=0):
        self.score = score
        self.player1 = Ninja("Michelanglo")
        self.player2 = Pirate("Jack Sparrow")

    def battle(self, pirate, ninja):
        print("ninja vs pirate")
        is_winner = False
        while not is_winner:
            if player1.health == 0 or player2.health == 0:
                is_winner = True
                player1_rand = random.radint(0,100)
                player2_rand = random.radint(0,100)

                pirate.health -= ninja.strength * (1 / ninja_rand)





if __name__ == "__main__":
    game = Game()
    game.battle()