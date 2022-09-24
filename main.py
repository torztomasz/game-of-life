"""
Program to run Game of Life visualization
"""

import sys
import pygame
from config.constants import (
    DEFAULT_SPEED,
    FRAMES_PER_SECOND,
    MAX_SPEED,
    MIN_SPEED,
    WINDOW_SIZE,
    WINDOW_TITLE,
)
from controllers.grid_controller import GridController


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

    controller = GridController(screen)
    controller.generate_random_grid_pattern()

    PAUSE = False
    SPEED = DEFAULT_SPEED
    FRAME_COUNT = 0

    while True:
        FRAME_COUNT += 1
        SHOULD_GENERATE_NEXT_GENERATION = (FRAME_COUNT + 1) % (10 - SPEED) == 0

        if not PAUSE and SHOULD_GENERATE_NEXT_GENERATION:
            controller.next_generation()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    controller.generate_random_grid_pattern()
                if event.key == pygame.K_SPACE:
                    PAUSE = not PAUSE
                if event.key == pygame.K_k:
                    if SPEED > MIN_SPEED:
                        SPEED -= 1
                if event.key == pygame.K_l:
                    if SPEED < MAX_SPEED:
                        SPEED += 1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(FRAMES_PER_SECOND)
