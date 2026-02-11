

class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initialized game statistics"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Reset statistics"""
        self.ship_left = self.settings.ship_limit
        self.ship_life = 2
        self.score = 0
