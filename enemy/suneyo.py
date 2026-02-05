import pygame
from PIL import Image

class Suneyo:
    """A class to manage the enemy boss."""
   
    def __init__(self, ai_game, ship):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Get ship size
        ship_width, ship_height = ship.rect.size

        # Load the PNG image
        png_image = Image.open("images/suneyo.png")

        # Resize to match ship size
        png_image = png_image.resize((ship_width, ship_height), Image.Resampling.LANCZOS)


        # Convert to bitmap (mode "1" or "L" depending on what you need)
        # "1" = 1-bit pixels, black and white
        # "L" = 8-bit pixels, grayscale
        bitmap_image = png_image.convert("1")

        # Save as BMP
        bitmap_image.save("images/suneyo.bmp")

        # Load the BMP into pygame
        self.image = pygame.image.load("images/suneyo.bmp")
        self.rect = self.image.get_rect()

        # Start position
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the enemy boss at its current location."""
        self.screen.blit(self.image, self.rect)