from random import randint

from Player import Player


class PlayerTeube(Player):
    def play(self):
        match randint(0, 10):
            case 0:
                self.LightCycle.turnLeft()
            case 1:
                self.LightCycle.turnRight()
            case _:
                pass
