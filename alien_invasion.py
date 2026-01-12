import sys
import  pygame
from settings.settings import Settings
from ship.ship import Ship
from enemy.enemy_boss import EnemyBoss
from enemy.alien import Alien
from bullets.bullets import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Display ship
        # self.alien = Alien(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Display Enemy
        # self.enemy = EnemyBoss(self, self.ship)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()

            # Get rid of bullets that have disappeared.
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Response to keypress and mouse event."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _full_screen_events(self, event):
        """handle the fullscreen"""
        if event.key == pygame.K_1:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
            )
        if event.key == pygame.K_2:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_height = self.screen.get_rect().height
            self.settings.screen_width = self.screen.get_rect().width

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_keyup_events(self,event):
        """Response to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_top = False
        elif event.key == pygame.K_UP:
            self.ship.moving_bottom = False

    def _check_keydown_events(self, event):
        """Response to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_top = True
        elif event.key == pygame.K_UP:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()
        else:
            self._full_screen_events(event)

    def _fire_bullets(self):
        """Firing Bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        # self.enemy.blitme()
        # self.alien.blitme()

    

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_fleet(self):
        """Create fleet of aliens"""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.x  = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2 * alien_width

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()