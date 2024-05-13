import pygame

class AnswerScreen:
    def __init__(self, width=1200, height=1000):
        self.screen_width = width
        self.screen_height = height
        self.background_color = (255, 255, 255)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Answer Screen")
        clock = pygame.time.Clock()
        running = True

        # Font settings
        font = pygame.font.Font(None, 36)
        text = font.render("", True, (0, 0, 0))
        text_rect = text.get_rect(center=screen.get_rect().center)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Move to a blank screen
                    running = False  # Exit this screen

            screen.fill(self.background_color)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
