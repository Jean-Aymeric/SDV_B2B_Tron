class Sprite:
    __character: chr

    def __init__(self, character: chr):
        self.__character = character

    @property
    def Character(self):
        return self.__character
