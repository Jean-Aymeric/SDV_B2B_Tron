from abc import ABC, abstractmethod

from LightCycle import LightCycle


class Player(ABC):
    __lightCycle: LightCycle | None

    def __init__(self):
        self.__lightCycle = None

    @property
    def LightCycle(self):
        return self.__lightCycle

    @LightCycle.setter
    def LightCycle(self, lightCycle: LightCycle):
        self.__lightCycle = lightCycle

    @abstractmethod
    def play(self):
        pass
