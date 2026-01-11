import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a float for the ship's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        # Movement flag start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        
        # Right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

        # Left
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 2

        # Up
        if self.moving_bottom and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed   # move UP

        # Down
        if self.moving_top and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed   # move DOWN


        # Update rect object from self.x and self.y.
        # self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)