import sys
import  pygame
from settings.settings import Settings
from ship.ship import Ship
from enemy.enemy_boss import EnemyBoss
from enemy.alien import Alien
from bullets.bullets import Bullet
from time import sleep
from stats.game_stats import GameStats

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Start Alien Invasion in an active state.
        self.game_active = True

        # Update screen count to stop updating the screen once the game is over
        self.update_screen_count = 0

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Create instace for Game Stats
        self.stats = GameStats(self)

        # Display ship
        # self.alien = Alien(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Display Enemy
        # self.enemy = EnemyBoss(self, self.ship)

        self.title_font = pygame.font.SysFont(None, 64)   # title
        self.desc_font = pygame.font.SysFont(None, 32)    # desc

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            if self.game_active:
                self.ship.update()
                # Get rid of bullets that have disappeared.
                self._update_bullets()
                self._update_aliens()
                self.clock.tick(60)
            else:
                self.bullets.empty()
                self.aliens.empty()
                self._game_over()
                self.update_screen_count += 1
            
            if self.update_screen_count < 2:
                self._update_screen()
    
    def _ship_hit(self):
        """Ship being hit by the alien"""
        print(f"ship_left:{self.stats.ship_left}")
        if self.stats.ship_left > 0:       
            # Decrement ships left.
            self.stats.ship_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False

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

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
     

    def _check_bullet_alien_collisions(self):
        """Response to bullet alien Collisions."""
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and creat new fleet.
            self.bullets.empty()
            self._create_fleet()


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
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
   
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create aliens and place it horizontally"""
        new_alien = Alien(self)
        new_alien.x  = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update aliens position"""
        self._check_fleet_edges()
        self.aliens.update()
    

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _game_over(self):
        """Game Over"""
        text_title = self.title_font.render("Game Over", True, (0, 0, 0))
        text_title_rect = text_title.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery - 30) )
        self.screen.blit(text_title, text_title_rect)

        text_desc = self.desc_font.render("Press 'Q' to exit the game", True, (0, 0, 0))
        text_desc_rect = text_desc.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery + 25))
        self.screen.blit(text_desc, text_desc_rect)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()