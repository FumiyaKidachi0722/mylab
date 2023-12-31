"""
This module contains the Player class for the game.
"""

import pygame


class Player(pygame.sprite.Sprite):
    """
    Represents a player object in the game.

    This class handles the behavior and movement of the player.
    """

    def __init__(self, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(width/2, height/2))

    def update(self, *args):
        """
        Update the player's position.
        This method is called to update the player's position based on keyboard input.
        """
        keys = pygame.key.get_pressed()  # キー入力を取得
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed  # 左キーが押されている場合、プレイヤーを左に移動
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed  # 右キーが押されている場合、プレイヤーを右に移動
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed  # 上キーが押されている場合、プレイヤーを上に移動
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed  # 下キーが押されている場合、プレイヤーを下に移動

        # プレイヤーの移動範囲をゲーム画面内に制限する
        self.rect.clamp_ip(pygame.Rect(0, 0, self.width, self.height))
