import pygame
from answer import AnswerScreen
import game 

class Game:
    def __init__(self, width=1200, height=1000):
        self.screen_width = width
        self.screen_height = height
        self.button_rect = pygame.Rect(500, 700, 200, 50)
        self.button_color = (0, 0, 0)
        self.button_text = "Answer Screen"

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("My Game")
        clock = pygame.time.Clock()
        print("its running")
        running = True

        # Load the background image
        background = pygame.image.load("background.jpg")
        background = pygame.transform.scale(background, (self.screen_width, self.screen_height))  # Scale image to match screen size

        # Load the image
        image = pygame.image.load("combined_image.png")
        image_rect = image.get_rect(center=screen.get_rect().center)

        # Initialize AnswerScreen
        answer_screen = AnswerScreen()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the button is clicked
                    if self.button_rect.collidepoint(event.pos):
                        answer_screen.run()  # Run AnswerScreen

            # Blit the background onto the screen
            screen.blit(background, (0, 0))

            # Blit the image onto the screen
            screen.blit(image, image_rect)

            # Draw the button
            pygame.draw.rect(screen, self.button_color, self.button_rect)
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.button_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.button_rect.center)
            screen.blit(text_surface, text_rect)

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    print("debug1")
    game = Game()
    game.run()
