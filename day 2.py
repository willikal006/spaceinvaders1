 def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        pass

    def update(self):
        """Update the alien"""
        pass

    def fire(self):
        """Fire a bullet"""
        pass

    def reset(self):
        """Reset the alien position"""
        pass


class PlayerBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        pass

    def update(self):
        """Update the bullet"""
        pass


class AlienBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        pass

    def update(self):
        """Update the bullet"""
        pass


