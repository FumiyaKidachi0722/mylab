"""
This module contains the Enemy class for the game.
"""

import pygame


class Enemy(pygame.sprite.Sprite):
    """
    Represents an enemy object in the game.

    This class handles the behavior and movement of enemies.
    """

    def __init__(self, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(width / 2, 0))

    def update(self, *args):
        """
        Update the enemy's position.
        This method is called to update the enemy's position based on its speed.
        """
        self.rect.y += self.speed  # 敵を下方向に移動させる
        if self.rect.bottom > self.height:
            self.kill()  # 敵が画面から消えたら敵を削除する
