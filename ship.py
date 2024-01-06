import pygame

class Ship(): 
    # playerShip class for control

    def __init__(self, screen):
        # initialize class, setting start position
        self.screen = screen

        # get ship image
        self.image = pygame.image.load("./assets/DurrrSpaceShip.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New life starts at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # show screen at current location
        self.screen.blit(self.image, self.rect)