import pygame
import random
import imgkit
from io import BytesIO
import questionmanagerdatabase

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1, 1))
        self.question_manager = questionmanagerdatabase.QuestionManager()
        self.questions = self.question_manager.getQuestionIds()

    def render_html_to_surface(self, html):
        config = imgkit.config(wkhtmltoimage=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
        img = imgkit.from_string(html, False, config=config)
        image_surface = pygame.image.load(BytesIO(img)).convert_alpha()
        return image_surface

    def combine_images_vertically(self, images):
        if not images:  # Check if images list is empty
            return pygame.Surface((1, 1))  # Return a small surface
        total_height = sum(image.get_height() for image in images)
        max_width = max(image.get_width() for image in images)
        combined_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)
        y_offset = 0
        for image in images:
            combined_surface.blit(image, (0, y_offset))
            y_offset += image.get_height()
        return combined_surface

    def start(self):
        print("Welcome to the Quiz Game!") 
        rand = random.randint(1,len(self.questions))
        question = self.question_manager.getQuestion(self.questions[rand])
        combined_images = []
        if 'stimulus' in question:
            stimulus = question["stimulus"]
            combined_images.append(self.render_html_to_surface(stimulus))
        if 'stem' in question:
            stem = question["stem"]
            combined_images.append(self.render_html_to_surface(stem))
        if 'answerOptions' in question:
            if len(question['answerOptions']) > 0: 
                for choice in question['answerOptions']:
                    combined_images.append(self.render_html_to_surface(choice['content']))
        
        combined_surface = self.combine_images_vertically(combined_images)
        pygame.image.save(combined_surface, "combined_image.png")
        pygame.quit()
        '''while True:
            print("\nSelect an option:")
            print("1. Start Quiz")
            print("2. Refresh Questions")
            print("3. Exit")
            choice = input("Enter your choice (1, 2, or 3): ")
            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.question_manager.refresh_questions()
                print("Refresh")
            elif choice == "3":
                print("Exit")
                pygame.quit()
                quit()
            else:
                print("Invalid choice. Please enter a valid option (1, 2, or 3).")'''

    def play_quiz(self):
        pass

game = Game()
game.start()
