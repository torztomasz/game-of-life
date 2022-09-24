"""
Module that is responsible for connection between Grid and GridView

Classes:

    GridController
"""

from random import random
from models.grid import Grid
from view.grid_view import GridView


class GridController:
    """
    A class to modify data in Grid and render it to screen

    ...

    Methods
    -------
    generate_random_grid_pattern():
        Generates random grid and sets it to self._grid

    count_neighbours(x, y):
        Returns count of neighbours for specific (x,y) cell

    next_generation():
        Creates next generation grid and draws it to screen
    """

    def __init__(self, screen):
        self._grid = Grid()
        self._view = GridView(screen)

    def generate_random_grid_pattern(self):
        """
        Generates random grid and sets it to self._grid

        Returns
        -------
        None
        """
        random_pattern = [
            [random() >= 0.6 for j in range(self._grid.rows)]
            for i in range(self._grid.columns)
        ]
        self._grid.set_grid(random_pattern)
        self._view.draw_grid(self._grid)

    def count_neighbours(self, x, y):
        """
        Returns count of neighbours for specific (x,y) cell

        Parameters
        ----------
        x : int
            Coordinate X of grid's cell
        y : int
            Coordinate Y of grid's cell

        Returns
        -------
        Int
        """
        count = 0
        neighbours = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        for _, coordinate in enumerate(neighbours):
            if self._grid.get_cell(coordinate[0], coordinate[1]):
                count += +1

        return count

    def next_generation(self):
        """
        Creates next generation grid and draws it to screen

        Returns
        -------
        None
        """
        new_grid = Grid()
        for x in range(self._grid.rows):
            for y in range(self._grid.columns):
                if self._grid.get_cell(x, y):
                    if (
                        self.count_neighbours(x, y) == 2
                        or self.count_neighbours(x, y) == 3
                    ):
                        new_grid.set_cell(x, y, True)
                    else:
                        new_grid.set_cell(x, y, False)
                else:
                    if self.count_neighbours(x, y) == 3:
                        new_grid.set_cell(x, y, True)
        self._grid = new_grid
        self._view.draw_grid(self._grid)
