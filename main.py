import pygame

class Game:
    def __init__(self, width=800, height=600):
        self.screen_width = width
        self.screen_height = height

    def run(self):
        
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("My Game")

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((255, 255, 255))  

           
            pygame.display.flip()

            
            clock.tick(30)

        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
