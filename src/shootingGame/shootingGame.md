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

### lesson 01

ゲームの実装
以下の Python スクリプトは、プレイヤーが敵を倒すシューティングゲームの基本的な実装を示しています：

#### main.py（メインのゲーム実行ファイル）：

```python
import pygame
import sys
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
running = True
while running:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
```

#### player.py

```python
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(width/2, height/2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, self.width, self.height))
```

#### bullet.py

```python
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
```

#### enemy.py

```python
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(width/2, 0))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.height:
            self.rect.bottom = 0
```

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

- [x] 敵に衝突しない
　　<details>
   - 衝突判定の処理を修正する必要があります。現在のコードでは敵と弾が衝突すると敵が消えてしまいますが、敵とプレイヤーの衝突も判定する必要があります。
   - 衝突判定にはpygame.sprite.spritecollide()関数を使用します。プレイヤーと敵のスプライトグループの衝突判定を行い、衝突があった場合にゲームオーバーの処理を追加します。
  </details>
- [ ] 敵の動きのバリエーションを追加する
  <details>
   - 敵の動きをランダムにするなど、バリエーションを追加するためには、敵のupdate()メソッドを修正します。
   - randomモジュールを使用して、敵の移動方向や速度をランダムに設定することができます。
  </details>
- [ ] 複数の敵を同時に出現させる
  <details>
   - Enemyクラスのインスタンスを複数作成し、それぞれの敵を別々のスプライトグループに追加します。
   - ゲームループ内で新しい敵を生成し、スプライトグループに追加することで、複数の敵を同時に出現させることができます。
  </details>
- [ ] 敵がプレイヤーに向かって攻撃する
  <details>
   - 敵がプレイヤーに向かって攻撃するためには、敵の座標とプレイヤーの座標の差を計算し、移動方向を設定します。
   - Playerクラスのインスタンスを敵のupdate()メソッドに渡し、敵がプレイヤーを追いかけるようにします。
  </details>
- [ ] スコアの追跡と表示
  <details>
   - スコアを管理する変数を追加し、敵を倒すたびにスコアを増やします。
   - スコアを表示するためには、Pygameの描画機能を使用してスコアを画面に表示します。
  </details>
- [ ] ゲームオーバーの条件と画面表示
  <details>
   - ゲームオーバーの条件を設定し、ゲームオーバー時には画面にゲームオーバーのメッセージを表示します。
   - ゲームオーバー時には、プレイヤーの操作を停止し、敵の出現を停止します。
  </details>
- [ ] 音楽や効果音の追加
  <details>
   - Pygameのサウンド機能を使用して、BGMや効果音を再生します。
   - ゲームの開始時や敵を倒した時など、適切なタイミングで音楽や効果音を再生することができます。
  </details>
- [ ] レベルアップやパワーアップの機能の追加
  <details>
   - レベルアップやパワーアップの機能を追加するには、プレイヤーの能力や敵の難易度を調整します。
   - レベルアップ時には、プレイヤーの移動速度や弾の速度を増加させるなどの変更を加えます。
  </details>