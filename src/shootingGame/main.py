"""
このモジュールはゲームのメインファイルです。
"""

import sys
import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy

# ゲームの定数
WIDTH, HEIGHT = 800, 600  # ゲームウィンドウの幅と高さ
FPS = 60  # フレームレート
PLAYER_SPEED = 5  # プレイヤーの移動速度
BULLET_SPEED = 10  # 弾の速度
ENEMY_SPEED = 2  # 敵の速度

# Pygameの初期化
pygame.init()

# ゲームウィンドウの作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# クロックの作成
clock = pygame.time.Clock()

# スプライトグループの作成
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# プレイヤーの作成
player = Player(WIDTH, HEIGHT, PLAYER_SPEED)
all_sprites.add(player)

# 敵の作成
enemy = Enemy(WIDTH, HEIGHT, ENEMY_SPEED)
all_sprites.add(enemy)
enemies.add(enemy)

# ゲームループ
RUNNING = True
while RUNNING:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.center, BULLET_SPEED)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # アップデート
    all_sprites.update()

    # 弾と敵の衝突のチェック
    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, enemies, True):
            bullet.kill()
            enemy = Enemy(WIDTH, HEIGHT, ENEMY_SPEED)
            all_sprites.add(enemy)
            enemies.add(enemy)

    # 描画
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # 描画したものを表示
    pygame.display.flip()

    # フレームレートの調整
    clock.tick(FPS)

# Pygameの終了
pygame.quit()
sys.exit()
