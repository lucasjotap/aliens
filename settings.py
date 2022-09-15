class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600 
        self.bg_color = (100, 100, 100)

        # Ship settings
        self.ship_speed_factor = 2.0

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 191, 0
        self.bullets_allowed = 3
        