from random import randint
from time import sleep

from Grid import Grid
from LightCycle import LightCycle
from Player import Player
from Screen import Screen


class Game:
    __grid: Grid
    __lightCycles: [LightCycle]
    __screen: Screen
    __players: [Player]

    def __init__(self):
        self.__grid = Grid(20, 80)
        self.__lightCycles = []
        self.__screen = Screen(self.__grid, self.__grid.Height, self.__grid.Width)
        self.__players = []

    def addPlayer(self, player: Player):
        self.__players.append(player)
        lightCycle = LightCycle(randint(0, self.__grid.Width), randint(0, self.__grid.Height), randint(0, 3))
        self.__lightCycles.append(lightCycle)
        player.LightCycle = lightCycle

    def play(self):
        running = True
        while running:
            for player in self.__players:
                player.play()
            for lightCycle in self.__lightCycles:
                lightCycle.move(self.__grid.Height, self.__grid.Width)
                lightCycle.Dead = self.__grid.isTileAWallAt(lightCycle.X, lightCycle.Y)
                self.__grid.setWallAt(lightCycle.X, lightCycle.Y)
                running &= not lightCycle.Dead
            self.__screen.display()
            sleep(0.1)
