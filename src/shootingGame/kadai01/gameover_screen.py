"""
This module contains the GameOverScreen class for the game.
"""
import pygame


class GameOverScreen(pygame.sprite.Sprite):
    """
    ゲームオーバースクリーンを表すクラスです。

    このクラスはゲームオーバースクリーンの表示と振る舞いを管理します。
    """

    @classmethod
    def draw(cls, screen):
        """
        指定された画面上にゲームオーバースクリーンを描画します。

        Args:
            screen: ゲームオーバースクリーンを描画する画面のサーフェス
        """
        pygame.font.init()  # フォントの初期化

        font = pygame.font.Font(None, 36)
        gameover_text = font.render("Game Over", True, (255, 255, 255))
        restart_text = font.render(
            "Press SPACE to restart", True, (255, 255, 255))
        return_text = font.render(
            "Press ENTER to quit", True, (255, 255, 255))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "exit"  # アプリを終了
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "start_screen"  # スタート画面を表示
                    elif event.key == pygame.K_RETURN:
                        pygame.quit()
                        return "exit"  # アプリを終了

            screen.fill((0, 0, 0))
            screen.blit(gameover_text, (screen.get_width() // 2 -
                                        gameover_text.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(restart_text, (screen.get_width() // 2 -
                                       restart_text.get_width() // 2, screen.get_height() // 2))
            screen.blit(return_text, (screen.get_width() // 2 -
                                      return_text.get_width() // 2, screen.get_height() // 2 + 50))
            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.font.quit()  # フォントの終了処理
        return "start_screen"
