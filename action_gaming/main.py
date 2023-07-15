import pygame

# ゲームの初期化
pygame.init()

# ゲームウィンドウの作成
screen = pygame.display.set_mode((800, 600))

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ゲームの描画
    screen.fill((0, 0, 0))
    pygame.display.flip()

# ゲームの終了
pygame.quit()
