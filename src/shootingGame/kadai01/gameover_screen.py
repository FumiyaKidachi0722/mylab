import pygame


class GameOverScreen(pygame.sprite.Sprite):
    clock = pygame.time.Clock()

    @classmethod
    def draw(cls, screen):
        pygame.font.init()  # フォントの初期化

        font = pygame.font.Font(None, 36)
        gameover_text = font.render("Game Over", True, (255, 255, 255))
        restart_text = font.render(
            "Press SPACE to restart", True, (255, 255, 255))

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
