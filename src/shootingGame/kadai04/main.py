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
from digit_patterns import digit_patterns

# ゲームの定数
WIDTH, HEIGHT = 800, 600  # ゲームウィンドウの幅と高さ
FPS = 60  # フレームレート
PLAYER_SPEED = 5  # プレイヤーの移動速度
BULLET_SPEED = 5  # 弾の速度
ENEMY_SPEED = 2  # 敵の速度
LIVES = 3  # プレイヤーの初期ライフ数


def draw_heart(surface, color, center, size):
    """
    ハートマークをドットで描画する関数
    """
    x, y = center
    r = size // 2
    for dy in range(size):
        for dx in range(size):
            if (
                (dx - r) ** 2 + (dy - r) ** 2 < r ** 2
                or (abs(dx - r) + abs(dy - r) < r)
                or (dy > r and (dx - r) ** 2 + (dy - size + r) ** 2 < r ** 2)
            ):
                surface.set_at((x - r + dx, y - r + dy), color)


def render_score_text(surface, font, position, score):
    """
    スコアをドットで描画する関数
    """
    x, y = position
    color = (255, 255, 255)  # スコアの色を設定

    # スコアを文字列に変換
    score_str = str(score)

    # 数字のドットパターンを拡大する倍率
    scale = 3

    # スコアをドットで描画
    for i, char in enumerate(score_str):
        if char.isdigit() and int(char) in digit_patterns:
            dot_pattern = digit_patterns[int(char)]

            # ドットを描画
            for dot_y in range(12):
                for dot_x in range(5):
                    if dot_pattern[dot_y][dot_x] == 1:
                        for dy in range(scale):
                            for dx in range(scale):
                                surface.set_at(
                                    (x + dot_x * scale + dx, y + dot_y * scale + dy), color)

        # 次の数字の描画位置に移動
        x += 7 * scale  # ドットパターンの幅 + ドットの間隔

    return surface


def run_game():
    """
    ゲームを実行するメイン関数です。
    """
    # Pygameの初期化
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.font.init()  # フォントの初期化
    font = pygame.font.SysFont("Arial", 36)

    # ハートマークの描画に使用するサイズと色
    heart_size = 20
    heart_color = (255, 0, 0)

    # クロックの作成
    clock = pygame.time.Clock()

    game_started = False  # ゲームが開始されたかどうかのフラグ

    # スプライトグループの作成
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # プレイヤーのライフを設定
    lives = LIVES

    # スコアを初期化
    score = 0

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
                    # スコアを加算
                    score += 1

                # プレイヤーと敵の衝突検出
                player_collisions = pygame.sprite.spritecollide(
                    player, enemies, True)
                if player_collisions:
                    lives -= 1
                    if lives == 0:
                        running = False

                all_sprites.draw(screen)  # 全てのスプライトを描画
                bullets.draw(screen)  # 弾丸のスプライトグループを描画
                enemies.draw(screen)  # 敵のスプライトグループを描画

                # ライフ表示の描画
                for i in range(lives):
                    draw_heart(screen, heart_color,
                               (WIDTH - 30 - i * 30, 10), heart_size)

                # スコアの描画
                score_position = (10, 10)
                screen = render_score_text(screen, font, score_position, score)

            else:
                StartScreen.draw(screen)  # スタート画面を描画

            pygame.display.flip()
            clock.tick(FPS)

    # ゲームオーバー画面の表示
    GameOverScreen.score = score  # スコアをGameoverScreenクラスのクラス変数にセット
    gameover_result = GameOverScreen.draw(screen)
    if gameover_result == "start_screen":
        run_game()  # スタート画面から再開

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run_game()
