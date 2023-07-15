"""
This module contains the Enemy class for the game.
"""

import random
import math
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
        self.direction = random.choice([-1, 1])  # ランダムな初期方向を選択
        self.start_x = random.randint(0, width)  # 出現位置のランダムなx座標を選択
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(self.start_x, 0))

    def update(self, *args):
        """
        Update the enemy's position.
        This method is called to update the enemy's position based on its speed.
        """
        self.rect.y += self.speed  # 敵を下方向に移動させる

        # 曲線を描くようにx座標を変化させる
        time = pygame.time.get_ticks() / 1000  # 時間の経過を取得
        amplitude = 100  # 曲線の振幅
        frequency = 2  # 曲線の周波数
        self.rect.x = self.start_x + self.direction * \
            amplitude * math.sin(frequency * time)

        # 画面内に収まるように位置を制限する
        self.rect.x = max(0, min(self.rect.x, self.width - self.rect.width))

        if self.rect.bottom > self.height:
            self.kill()  # 敵が画面から消えたら敵を削除する
