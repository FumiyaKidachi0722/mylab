import pygame


class StartScreen(pygame.sprite.Sprite):
    clock = pygame.time.Clock()

    @classmethod
    def draw(cls, screen):
        pygame.font.init()  # フォントの初期化

        font = pygame.font.Font(None, 36)
        title_text = font.render("Shooting Game", True, (255, 255, 255))
        start_text = font.render("Press SPACE to start", True, (255, 255, 255))

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
                        title_text.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(start_text, (screen.get_width() // 2 -
                        start_text.get_width() // 2, screen.get_height() // 2))
            pygame.display.flip()
            cls.clock.tick(60)

        pygame.font.quit()  # フォントの終了処理
