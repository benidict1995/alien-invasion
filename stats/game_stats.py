

class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initialized game statistics"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Reset statistics"""
        self.ship_left = 3
        self.ship_life = 3
        self.score = 0
        self.level = 1
