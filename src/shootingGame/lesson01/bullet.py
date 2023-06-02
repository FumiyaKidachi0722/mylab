"""
This module contains the Bullet class for the game.
"""

import pygame


class Bullet(pygame.sprite.Sprite):
    """
    Represents a bullet object in the game.

    This class handles the behavior and movement of bullets.
    """

    def __init__(self, pos, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        """
        Update the bullet's position.
        This method is called to update the bullet's position based on its speed.
        """
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
