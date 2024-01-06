import sys

import pygame

from settings import Settings


def startGame():
    # starts game and create display
    pygame.init()
    gameSettings = Settings()
    screen = pygame.display.set_mode((gameSettings.screenWidth, gameSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    # Set background color
    bgColor = gameSettings.bgColor

    # begin gameplay
    while True:
        # listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bgColor)

        # Refresh screen
        pygame.display.flip()


startGame()
