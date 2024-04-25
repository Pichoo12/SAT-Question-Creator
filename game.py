import pygame
import random
import imgkit
from io import BytesIO
import questionmanagerdatabase

class Game:
    def __init__(self):
        self.question_manager = questionmanagerdatabase.QuestionManager()
        self.questions = self.question_manager.getQuestionIds()

    def render_html_to_image(self, html, filename="output.png"):
        config = imgkit.config(wkhtmltoimage=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
        img = imgkit.from_string(html, False, config=config)
        image_surface = pygame.image.load(BytesIO(img))
        
        # Save the image as PNG
        pygame.image.save(image_surface, filename)
        
        return image_surface


    def start(self):
        print("Welcome to the Quiz Game!") 
        print(self.question_manager.getQuestion(self.questions[random.randint(1,len(self.questions))]))
        self.render_html_to_image(self.question_manager.getQuestion(self.questions[random.randint(1,len(self.questions))])['stem'])
        while True:
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
                quit()
            else:
                print("Invalid choice. Please enter a valid option (1, 2, or 3).")

    def play_quiz(self):
        # Here you can implement the quiz functionality
        pass

# Initialize and start the game
game = Game()
game.start()
