import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Manage alient class"""

    def __init__(self, ai_game):
        """Initialized the alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the alien image and its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Update the alien's position"""

    def blitme(self):
        """Draw the alien and its current location"""
        self.screen.blit(self.image, self.rect)
