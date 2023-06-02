# シューティングゲームの作成: Python と Pygame を使用したガイド

## 必要なツール

- Anaconda
- Python
- Pygame

## セットアップ

1. Anaconda のインストール

   - Anaconda はこちらからダウンロードできます：https://www.anaconda.com/products/distribution

   - インストール手順はこちらを参照してください：https://docs.anaconda.com/anaconda/install/

1. 新しい環境の作成

   - Anaconda Navigator を開き、"Environments"タブを選択します。

   - "Create"ボタンをクリックし、新しい環境の名前と Python のバージョンを選択します（Python 3.x を推奨）。

1. Pygame のインストール

   - 新しく作成した環境を選択し、"Open Terminal"をクリックします。

   - ```
     $ mkdir shootingGame
     ```

   - ```
     $ cd shootingGame
     ```

   - 開いたターミナルに次のコマンドを入力して、Pygame をインストールします：

     ```
     $ pip install pygame
     ```

     - 再起動
     - vscode
     - ```
       $ conda activate shootingGame
       ```

### lesson 01

ゲームの実装
以下の Python スクリプトは、プレイヤーが敵を倒すシューティングゲームの基本的な実装を示しています：

<details><summary>main.py</summary>

```python
"""
This module contains the main.
"""

import sys
import pygame
from pygame.locals import QUIT, K_SPACE
from player import Player
from bullet import Bullet
from enemy import Enemy

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
            # ゲーム開始
            game_started = True

            # プレイヤーの作成
            player = Player(WIDTH, HEIGHT, PLAYER_SPEED)
            all_sprites.add(player)

            # 敵の作成
            enemy = Enemy(WIDTH, HEIGHT, ENEMY_SPEED)
            all_sprites.add(enemy)
            enemies.add(enemy)

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

            pygame.display.flip()
            clock.tick(FPS)

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
```

</details>

<details><summary>player.py</summary>

```python
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
```

</details>

<details><summary>bullet.py</summary>

```python
"""
This module contains the Bullet class for the game.
"""

import pygame


class Bullet(pygame.sprite.Sprite):
    """
    Represents a bullet object in the game.

    This class handles the behavior and movement of bullets.
    """

    def __init__(self, pos, speed, enemies):
        super().__init__()
        self.speed = speed
        self.enemies = enemies
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

    def update(self, *args):
        """
        Update the bullet's position.
        This method is called to update the bullet's position based on its speed.
        """
        self.rect.y -= self.speed  # 弾を上方向に移動させる
        if self.rect.bottom < 0:
            self.kill()  # 弾が画面外に出たら弾を削除する
```

</details>

<details><summary>enemy.py</summary>

```python
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
```

</details>


## 実行

```
$ python main.py
```

## ゲームの説明

- このゲームでは、プレイヤーは四方に移動することができ、スペースキーを押すと弾を発射します。
- 弾と敵が衝突すると、弾と敵が消え、新しい敵がスクリーン上部から出現します。
- 敵はスクリーンを下に向かって移動し、スクリーンの下部に達すると再び上部から出現します。

## ゲーム開発のヒント

- このゲームは基本的なシューティングゲームで、より複雑なゲームを作成するためには、敵の動きのバリエーション、複数の敵、敵からの反撃、スコアの追跡、ゲームオーバーの条件など、さらに多くの要素を追加することができます。
- ゲーム開発にはテストとデバッグが重要な役割を果たします。ゲームが期待通りに動作しない場合やバグが見つかった場合は、問題を修正して再度テストを行います。最終的には、コードのリファクタリングと最適化を行い、効率的で読みやすいコードにすることが重要です。

---

# 課題
1. - [ ]  [スタートとエンド画面](#始まりと終わり)
    <details>
    - 
    <details>

- [x] [敵に衝突しない](#敵に衝突しない)
　　<details>
   - 衝突判定の処理を修正する必要があります。現在のコードでは敵と弾が衝突すると敵が消えてしまいますが、敵とプレイヤーの衝突も判定する必要があります。
   - 衝突判定にはpygame.sprite.spritecollide()関数を使用します。プレイヤーと敵のスプライトグループの衝突判定を行い、衝突があった場合にゲームオーバーの処理を追加します。
  </details>
- [ ] [敵の動きのバリエーションを追加する](#敵の動きのバリエーションを追加する)
  <details>
   - 敵の動きをランダムにするなど、バリエーションを追加するためには、敵のupdate()メソッドを修正します。
   - randomモジュールを使用して、敵の移動方向や速度をランダムに設定することができます。
  </details>
- [ ] [複数の敵を同時に出現させる](#複数の敵を同時に出現させる)
  <details>
   - Enemyクラスのインスタンスを複数作成し、それぞれの敵を別々のスプライトグループに追加します。
   - ゲームループ内で新しい敵を生成し、スプライトグループに追加することで、複数の敵を同時に出現させることができます。
  </details>
- [ ] [敵がプレイヤーに向かって攻撃する](#敵がプレイヤーに向かって攻撃する)
  <details>
   - 敵がプレイヤーに向かって攻撃するためには、敵の座標とプレイヤーの座標の差を計算し、移動方向を設定します。
   - Playerクラスのインスタンスを敵のupdate()メソッドに渡し、敵がプレイヤーを追いかけるようにします。
  </details>
- [ ] [スコアの追跡と表示](#スコアの追跡と表示)
  <details>
   - スコアを管理する変数を追加し、敵を倒すたびにスコアを増やします。
   - スコアを表示するためには、Pygameの描画機能を使用してスコアを画面に表示します。
  </details>
- [ ] [ゲームオーバーの条件と画面表示](#ゲームオーバーの条件と画面表示)
  <details>
   - ゲームオーバーの条件を設定し、ゲームオーバー時には画面にゲームオーバーのメッセージを表示します。
   - ゲームオーバー時には、プレイヤーの操作を停止し、敵の出現を停止します。
  </details>
- [ ] [音楽や効果音の追加](#音楽や効果音の追加)
  <details>
   - Pygameのサウンド機能を使用して、BGMや効果音を再生します。
   - ゲームの開始時や敵を倒した時など、適切なタイミングで音楽や効果音を再生することができます。
  </details>
- [ ] [レベルアップやパワーアップの機能の追加](#レベルアップやパワーアップの機能の追加)
  <details>
   - レベルアップやパワーアップの機能を追加するには、プレイヤーの能力や敵の難易度を調整します。
   - レベルアップ時には、プレイヤーの移動速度や弾の速度を増加させるなどの変更を加えます。
  </details>

## 始まりと終わり
  1. スタート画面とゲームオーバー画面を作成

  <details><summary>start_screen.py</summary>

```python
"""
This module contains the StartScreen class for the game.
"""
import pygame


class StartScreen(pygame.sprite.Sprite):
    """
    Represents the start screen of the game.

    This class handles the drawing and behavior of the start screen.
    """

    clock = pygame.time.Clock()

    @classmethod
    def draw(cls, screen):
        """
        Draw the start screen.

        This method draws the title and start text on the screen.
        """

        pygame.font.init()  # フォントの初期化

        font = pygame.font.Font(None, 36)
        title_text = font.render(
            "Shooting Game", True, (255, 255, 255))  # タイトルテキストの作成
        start_text = font.render(
            "Press SPACE to start", True, (255, 255, 255))  # 開始テキストの作成

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            screen.fill((0, 0, 0))
            screen.blit(title_text, (screen.get_width() // 2 -
                        title_text.get_width() // 2, screen.get_height() // 2 - 50))  # タイトルテキストの描画
            screen.blit(start_text, (screen.get_width() // 2 -
                        start_text.get_width() // 2, screen.get_height() // 2))  # 開始テキストの描画
            pygame.display.flip()
            cls.clock.tick(60)

        pygame.font.quit()  # フォントの終了処理
```

  </details>

  <details><summary>gameover_screen.py</summary>

```python
"""
This module contains the GameOverScreen class for the game.
"""
import pygame


class GameOverScreen(pygame.sprite.Sprite):
    """
    ゲームオーバースクリーンを表すクラスです。

    このクラスはゲームオーバースクリーンの表示と振る舞いを管理します。
    """

    clock = pygame.time.Clock()

    @classmethod
    def draw(cls, screen):
        """
        指定された画面上にゲームオーバースクリーンを描画します。

        Args:
            screen: ゲームオーバースクリーンを描画する画面のサーフェス
        """
        pygame.font.init()  # フォントの初期化

        font = pygame.font.Font(None, 36)
        gameover_text = font.render("ゲームオーバー", True, (255, 255, 255))
        restart_text = font.render(
            "スペースキーを押して再開", True, (255, 255, 255))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            screen.fill((0, 0, 0))
            screen.blit(gameover_text, (screen.get_width(
            ) // 2 - gameover_text.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(restart_text, (screen.get_width() // 2 -
                        restart_text.get_width() // 2, screen.get_height() // 2))
            pygame.display.flip()
            cls.clock.tick(60)

        pygame.font.quit()  # フォントの終了処理
```

  </details>

  <details><summary>main.py</summary>

```python
...
from start_screen import StartScreen
from gameover_screen import GameOverScreen

...

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
            
...

            else:
                StartScreen.draw(screen)  # スタート画面を描画

...

    # ゲームオーバー画面の表示
    GameOverScreen.draw(screen)
```

  </details>

## 敵に衝突しない
  1. Player クラスに check_collision() メソッドを追加します。このメソッドは、プレイヤーと敵キャラの衝突をチェックします。
  1. Enemy クラスに check_collision() メソッドを追加します。このメソッドは、敵キャラと弾の衝突をチェックします。
  1. Player クラスと Enemy クラスの update() メソッド内で、衝突チェックの呼び出しを追加します。
  1. 弾と敵の衝突をチェックする部分で、衝突した敵キャラを削除するのではなく、プレイヤーとの衝突判定を行い、衝突した場合はゲームを終了するようにします。

<details><summary>main.py</summary>
  ```python
  ```

</details>

<details><summary>player.py</summary>
  ```python
  ```
</details>


<details><summary>enemy.py</summary>
  ```python
  ```
</details>


## 敵の動きのバリエーションを追加する
* 

## 複数の敵を同時に出現させる
* 

## 敵がプレイヤーに向かって攻撃する
* 

## スコアの追跡と表示
* 

## ゲームオーバーの条件と画面表示
* 

## 音楽や効果音の追加
* 

## レベルアップやパワーアップの機能の追加
* 
