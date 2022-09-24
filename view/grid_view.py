"""
Module to show Grid model on screen

Classes:

    GridView
"""


import pygame

from config.constants import BLACK, CELL_SIZE
from models.grid import Grid


class GridView:
    """
    Class to render grid to the pygame view

    ...

    Methods
    -------
    rerender():
        Rerenders screen content

    draw_grid(grid):
        Draws grid to the screen
    """

    def __init__(self, screen):
        self._screen = screen
        self._background = pygame.Surface(screen.get_size())

    def rerender(self):
        """
        Rerenders screen content

        Returns
        -------
        None
        """
        self._screen.blit(self._background, (0, 0))
        pygame.display.flip()

    def draw_grid(self, grid: Grid):
        """
        Draws grid to the screen
        Every cell will have its own color

        Parameters
        ----------
        grid : Grid
            Grid that should be rendered to the screen

        Returns
        -------
        None
        """

        def get_cell_color(x, y, columns, rows):
            column_factor = x / columns * 128
            row_factor = y / rows * 128
            return (
                255 - column_factor,
                255 - column_factor - row_factor,
                255 - row_factor,
            )

        self._background.fill(BLACK)
        columns = grid.columns
        rows = grid.rows
        for x, _ in enumerate(grid.grid):
            for y, _ in enumerate(grid.grid[x]):
                if grid.grid[x][y]:
                    rect = pygame.Rect(
                        x * CELL_SIZE,
                        y * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                    )
                    color = get_cell_color(x, y, columns, rows)
                    pygame.draw.rect(self._background, color, rect)
        self.rerender()
