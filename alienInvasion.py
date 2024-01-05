import sys

import pygame


def startGame():
    # starts game and create display
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # begin gameplay
    while True:
        # listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Refresh screen
        pygame.display.flip()

startGame()
