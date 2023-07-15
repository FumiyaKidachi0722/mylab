import random
import pygame
from pygame.locals import *

# 初期設定
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bingo Galagar")

# 数字のリスト
numbers = list(range(1, 101))
random.shuffle(numbers)

# ガラガラのボタン
button_image = pygame.image.load("./images/bingo.jpg")  # ボタンの画像ファイルを指定
button_rect = button_image.get_rect()
button_rect.center = (screen_width // 2, screen_height // 2)

# 端に表示される数字のリスト
displayed_numbers = []

# ビンゴカードのスクロール用のパラメータ
card_x, card_y = 20, 20
card_width, card_height = 300, screen_height - 40
scroll_speed = 2

# フォントの設定
font = pygame.font.Font(None, 36)  # フォントとサイズを適宜指定

scroll_offset = 0  # スクロールのオフセット

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if numbers:
                    number = numbers.pop()
                    displayed_numbers.append(number)

    screen.fill((255, 255, 255))  # 背景を白に設定
    screen.blit(button_image, button_rect)  # ボタンを描画

    # 端に表示される数字の描画
    text_y = card_y + scroll_offset  # 数字の表示位置（Y座標）
    for number in displayed_numbers:
        text = font.render(str(number), True, (0, 0, 0))  # 数字をレンダリング
        text_rect = text.get_rect()
        text_rect.topleft = (card_x, text_y)
        if text_y + text_rect.height > card_y + card_height:
            text_rect.left = card_x + card_width + 20  # 右の行に表示
            text_y = card_y + scroll_offset
        screen.blit(text, text_rect)  # 数字を描画
        text_y += text_rect.height  # 次の数字の表示位置を調整

    # スクロールの制御
    total_height = len(displayed_numbers) * \
        text_rect.height if displayed_numbers else 0
    if total_height > card_height:
        if scroll_offset < 0:
            scroll_offset += scroll_speed
        elif scroll_offset + total_height > card_height:
            scroll_offset -= scroll_speed

    pygame.display.update()

pygame.quit()
