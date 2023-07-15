import pygame
import sys
from stages.stage1 import draw_stage1
from stages.stage2 import draw_stage2
from stages.stage3 import draw_stage3

# ゲームの初期化
pygame.init()

# ウィンドウのサイズ
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# ウィンドウの作成
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Super Mario-like Game")

# ステージの選択肢
stages = ["Stage 1", "Stage 2", "Stage 3"]

# ステージの描画


def draw_stage(stage_number):
    if stage_number == 1:
        draw_stage1(screen)
    elif stage_number == 2:
        draw_stage2(screen)
    elif stage_number == 3:
        draw_stage3(screen)

# ゲームループ


def game_loop():
    selected_stage = 0
    arrow_pos = 0

    while True:
        screen.fill(WHITE)

        # ステージ選択画面
        if selected_stage == 0:
            for i, stage in enumerate(stages):
                font = pygame.font.SysFont(None, 48)
                text = font.render(stage, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (WINDOW_WIDTH // 2, 100 + i * 50)
                screen.blit(text, text_rect)

                # 矢印の描画
                if i == arrow_pos:
                    arrow = font.render("->", True, BLUE)
                    arrow_rect = arrow.get_rect()
                    arrow_rect.center = (WINDOW_WIDTH // 2 - 50, 100 + i * 50)
                    screen.blit(arrow, arrow_rect)

        # ステージ描画
        else:
            draw_stage(selected_stage)

        pygame.display.flip()

        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # 矢印の位置を上に移動
                    arrow_pos = (arrow_pos - 1) % len(stages)
                elif event.key == pygame.K_DOWN:
                    # 矢印の位置を下に移動
                    arrow_pos = (arrow_pos + 1) % len(stages)
                elif event.key == pygame.K_RETURN:
                    # ステージ決定
                    if selected_stage == 0:
                        selected_stage = arrow_pos + 1
                    else:
                        return selected_stage

# メイン関数


def main():
    while True:
        selected_stage = game_loop()

        # ゲームプレイ
        if selected_stage != 0:
            print("Start Game: Stage", selected_stage)
            # ゲームの実行処理を記述


# ゲームの実行
if __name__ == "__main__":
    main()
