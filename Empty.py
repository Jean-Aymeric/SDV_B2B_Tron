from Sprite import Sprite
from Tile import Tile


class Empty(Tile):
    def __init__(self):
        super().__init__(Sprite("."))
