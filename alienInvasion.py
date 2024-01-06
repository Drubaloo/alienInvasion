import sys

import pygame

from settings import Settings
from ship import Ship

def startGame():
    # starts game and create display
    pygame.init()
    # Instance of settings
    gameSettings = Settings()
    screen = pygame.display.set_mode((gameSettings.screenWidth, gameSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    # Set background color
    bgColor = gameSettings.bgColor

    # make ship
    ship = Ship(screen)

    # begin gameplay
    while True:
        # listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # change screen and show ship
        screen.fill(bgColor)
        ship.blitme()
        # Refresh screen
        pygame.display.flip()


startGame()
