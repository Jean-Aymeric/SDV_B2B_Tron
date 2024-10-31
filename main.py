from Game import Game
from PlayerTeube import PlayerTeube

game = Game()
game.addPlayer(PlayerTeube())
game.addPlayer(PlayerTeube())

game.play()
