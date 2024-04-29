import pygame
import questionmanagerdatabase
import game
import time
#import sound 

print("debug2")

class Game:
    def __init__(self, width=1200, height=1000):
        self.screen_width = width
        self.screen_height = height

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("My Game")
        clock = pygame.time.Clock()
        print ("its running")
        running = True

        # Load the image
        image = pygame.image.load("combined_image.png")
        image_rect = image.get_rect(center=screen.get_rect().center)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((255, 255, 255))

            # Blit the image onto the screen
            screen.blit(image, image_rect)

            pygame.display.flip()

            clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    print("debug1")
    game = Game()
    game.run()