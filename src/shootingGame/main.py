"""
This module contains the main.
"""

import sys
import pygame
from pygame.locals import QUIT, K_SPACE
from player import Player
from bullet import Bullet
from enemy import Enemy
from start_screen import StartScreen
from gameover_screen import GameOverScreen

# ゲームの定数
WIDTH, HEIGHT = 800, 600  # ゲームウィンドウの幅と高さ
FPS = 60  # フレームレート
PLAYER_SPEED = 5  # プレイヤーの移動速度
BULLET_SPEED = 5  # 弾の速度
ENEMY_SPEED = 2  # 敵の速度


def run_game():
    """
    ゲームを実行するメイン関数です。
    """
    # Pygameの初期化
    pygame.init()
    pygame.font.init()  # フォントの初期化
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # クロックの作成
    clock = pygame.time.Clock()

    game_started = False  # ゲームが開始されたかどうかのフラグ

    # スプライトグループの作成
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # ゲームループ
    running = True
    bullet_fired = False  # 弾丸が発射されたかどうかのフラグ

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        if not game_started:
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                # ゲーム開始
                game_started = True
                # ゲームオーバー画面をリセット
                all_sprites.empty()
                bullets.empty()
                enemies.empty()

                # プレイヤーの作成
                player = Player(WIDTH, HEIGHT, PLAYER_SPEED)
                all_sprites.add(player)

                # 敵の作成
                enemy = Enemy(WIDTH, HEIGHT, ENEMY_SPEED)
                all_sprites.add(enemy)
                enemies.add(enemy)
            else:
                screen.fill((0, 0, 0))
                StartScreen.draw(screen)  # スタート画面を描画
                pygame.display.flip()
                clock.tick(FPS)
                continue

        if running:
            keys = pygame.key.get_pressed()
            if keys[K_SPACE] and not bullet_fired:
                # スペースキーが押下されたら弾丸を発射
                bullet = Bullet(player.rect.center, BULLET_SPEED, enemies)
                all_sprites.add(bullet)
                bullets.add(bullet)
                bullet_fired = True
            elif not keys[K_SPACE]:
                bullet_fired = False

            screen.fill((0, 0, 0))

            if game_started:
                all_sprites.update()  # スプライトの位置を更新

                # 敵が画面から消えた場合に新たに敵を生成する
                if len(enemies) == 0:
                    enemy = Enemy(WIDTH, HEIGHT, ENEMY_SPEED)
                    all_sprites.add(enemy)
                    enemies.add(enemy)

                # 衝突検出
                collisions = pygame.sprite.groupcollide(
                    enemies, bullets, True, True)
                for _ in collisions:
                    # 敵を再度生成してスプライトグループに追加する
                    enemy = Enemy(WIDTH, HEIGHT, ENEMY_SPEED)
                    all_sprites.add(enemy)
                    enemies.add(enemy)

                all_sprites.draw(screen)  # 全てのスプライトを描画
                bullets.draw(screen)  # 弾丸のスプライトグループを描画
                enemies.draw(screen)  # 敵のスプライトグループを描画
            else:
                StartScreen.draw(screen)  # スタート画面を描画

            pygame.display.flip()
            clock.tick(FPS)

    # ゲームオーバー画面の表示
    GameOverScreen.draw(screen)

    pygame.quit()
    sys.exit()


def update(self, *args):
    """
    敵の位置を更新する関数です。
    敵の位置をスピードに基づいて更新するために呼び出されます。
    """
    self.rect.y += self.speed
    if self.rect.top > self.height:
        self.rect.bottom = 0

    # 衝突検出
    collisions = pygame.sprite.spritecollide(self, args[0], True)
    if collisions:
        self.kill()


if __name__ == "__main__":
    run_game()
