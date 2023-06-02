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
