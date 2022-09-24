"""
Module that contains class representing grid

Classes:

    Grid
"""

from config.constants import CELL_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH


class Grid:
    """
    A class to represent grid that gets rendered to screen

    ...

    Methods
    -------
    set_cell(x, y, state):
        Sets state of specific (x,y) cell

    get_cell(x, y):
        Gets state of specific (x,y) cell

    set_grid(grid):
        Sets grid of this model
    """

    def __init__(self):
        self.columns = int(WINDOW_WIDTH / CELL_SIZE)
        self.rows = int(WINDOW_HEIGHT / CELL_SIZE)
        if self.columns < 10 or self.rows < 10:
            raise Exception(
                "Grid can not have less than 10 columns. "
                + "Tweak CELL_SIZE in constants to fix this"
            )
        self.grid = [[False for j in range(self.rows)] for i in range(self.columns)]

    def set_cell(self, x, y, state):
        """
        Sets state of specific (x,y) cell

        Parameters
        ----------
        x : int
            Coordinate X of grid's cell
        y : int
            Coordinate Y of grid's cell
        state: bool
            State that should be set to (x,y) cell

        Returns
        -------
        None
        """
        self.grid[x][y] = state

    def get_cell(self, x, y):
        """
        Gets state of specific (x,y) cell

        Parameters
        ----------
        x : int
            Coordinate X of grid's cell
        y : int
            Coordinate Y of grid's cell

        Returns
        -------
        Bool
        """
        if x < 0 or y < 0 or x >= self.columns or y >= self.rows:
            return False

        return self.grid[x][y]

    def set_grid(self, grid):
        """
        Sets grid of this model

        Parameters
        ----------
        grid: list[list[bool]]
            Grid that should be set as this object grid

        Returns
        -------
        None
        """
        self.grid = grid
