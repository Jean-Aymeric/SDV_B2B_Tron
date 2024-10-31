from Grid import Grid


class Screen:
    __height: int
    __width: int
    __grid: Grid

    def __init__(self, grid: Grid, height: int, width: int):
        self.__width = width
        self.__height = height
        self.__grid = grid

    def display(self) -> None:
        for row in range(self.__grid.Height):
            for column in range(self.__grid.Width):
                print(self.__grid.getTileAt(column, row).Sprite.Character, end="")
            print()
