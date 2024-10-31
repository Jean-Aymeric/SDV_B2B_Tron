from Tile import Tile


class LightCycle(Tile):
    __x: int
    __y: int
    __dead: bool
    __direction: int

    def __init__(self, x: int, y: int, direction: int):
        super().__init__("A")
        self.__x = x
        self.__y = y
        self.__dead = False
        self.__direction = direction

    def move(self, height: int, width: int):
        if self.__direction == 0:
            self.__y -= 1
        elif self.__direction == 1:
            self.__x += 1
        elif self.__direction == 2:
            self.__y += 1
        else:
            self.__x -= 1
        self.__x = self.__x % width
        self.__y = self.__y % height

    def turnLeft(self):
        self.__direction = (self.__direction + 3) % 4

    def turnRight(self):
        self.__direction = (self.__direction + 1) % 4

    @property
    def X(self):
        return self.__x

    @property
    def Y(self):
        return self.__y

    @property
    def Dead(self):
        return self.__dead

    @Dead.setter
    def Dead(self, dead: bool):
        self.__dead = dead

    @property
    def Direction(self):
        return self.__direction
