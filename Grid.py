from Empty import Empty
from Tile import Tile
from Wall import Wall


class Grid:
    __tiles: [[Tile]]
    __height: int
    __width: int

    def __init__(self, height: int, width: int):
        self.__width = width
        self.__height = height
        self.__tiles = []
        empty = Empty()
        self.__wall = Wall()
        for row in range(self.__height):
            self.__tiles.append([empty] * self.__width)

    @property
    def Height(self):
        return self.__height

    @property
    def Width(self):
        return self.__width

    def setWallAt(self, x: int, y: int) -> None:
        self.__tiles[y][x] = self.__wall

    def isTileAWallAt(self, x: int, y: int):
        return self.__tiles[y][x] == self.__wall

    def getTileAt(self, x: int, y: int):
        return self.__tiles[y][x]
