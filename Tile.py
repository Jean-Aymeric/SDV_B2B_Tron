from abc import ABC

from Sprite import Sprite


class Tile(ABC):
    __sprite: Sprite

    def __init__(self, sprite: Sprite):
        self.__sprite = sprite

    @property
    def Sprite(self):
        return self.__sprite

    @Sprite.setter
    def Sprite(self, sprite: Sprite):
        self.__sprite = sprite
