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
