import tkinter as tk
import pygame

from player import Player
from enemy import Enemy
from bullets import Bullet

WHITE = (255, 255, 255)
FPS = 60

class QuizGame:
    def __init__(self, q):
        self.questions = q  # the dictionary is then received and stored
        self.SCREENWIDTH = 800
        self.SCREENHEIGHT = 600
        self.current_question_index = 0
        self.question_keys = list(self.questions.keys())
        self.current_correct_answer = None

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.set_caption('Quiz Game')
        self.running = True
        self.clock = pygame.time.Clock()
        # font for on-screen quiz text display
        self.font = pygame.font.SysFont(None, 26)
        self.question_text_lines = []
        self.initialize()
        
    def initialize(self):
        self.playerSpriteGroup = pygame.sprite.Group()
        self.player = Player(400, 300)
        self.playerSpriteGroup.add(self.player)

        # bullets fired by the player
        self.bulletsSpriteGroup = pygame.sprite.Group()
        
        self.enemiesSpriteGroup = pygame.sprite.Group()
        self.init_enemies()
        
        # Display the first question
        self.display_question()
    
    def display_question(self):
        """Display the current question and its choices"""
        if self.current_question_index >= len(self.question_keys):
            print("\n=== Quiz Complete! ===")
            self.running = False
            return
        
        question_key = self.question_keys[self.current_question_index]
        question_data = self.questions[question_key]
        
        # print(f"\n=== Question {self.current_question_index + 1} ===")
        # print(f"{question_data['question']}")
        # print(f"Enemy A: {question_data['A']}")
        # print(f"Enemy B: {question_data['B']}")
        # print(f"Enemy C: {question_data['C']}")
        # print(f"Enemy D: {question_data['D']}")
        
        self.current_correct_answer = question_data['correct']
        self.current_question_text = f"{self.current_question_index + 1}. {question_data['question']}"
        self.current_answer_options = {
            'A': question_data['A'],
            'B': question_data['B'],
            'C': question_data['C'],
            'D': question_data['D'],
        }

        # Prepare wrapped content for rendering.
        self.question_text_lines = [
            f"Question {self.current_question_index + 1}/{len(self.question_keys)}",
        ]

        self.question_text_lines.extend(self.wrap_text(self.current_question_text, self.SCREENWIDTH - 20))

        choices_line = (
            f"A: {self.current_answer_options['A']}    "
            f"B: {self.current_answer_options['B']}    "
            f"C: {self.current_answer_options['C']}    "
            f"D: {self.current_answer_options['D']}"
        )

        self.question_text_lines.append(self.truncate_text(choices_line, self.SCREENWIDTH - 20))

    def wrap_text(self, text, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''

        for word in words:
            candidate = f"{current_line} {word}".strip()
            if self.font.size(candidate)[0] <= max_width:
                current_line = candidate
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    def truncate_text(self, text, max_width):
        if self.font.size(text)[0] <= max_width:
            return text

        ellipsis = '...'
        candidate = text
        while candidate and self.font.size(candidate + ellipsis)[0] > max_width:
            candidate = candidate[:-1]

        return (candidate + ellipsis) if candidate else ellipsis
    
    def init_enemies(self):
        amtOfEnemies = 4

        # Spread enemies evenly around the screen center
        spacing = 150
        center_x = self.SCREENWIDTH // 2
        start_x = center_x - (amtOfEnemies - 1) * spacing // 2
        y = self.SCREENHEIGHT // 2 - 100  # spawn near vertical center

        for i in range(amtOfEnemies):
            x = start_x + i * spacing
            enemy = Enemy(i,x, y)
            self.enemiesSpriteGroup.add(enemy)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Player movement + shooting
        bullet = self.player.handle_input(keys)
        if bullet:
            self.bulletsSpriteGroup.add(bullet)

        self.playerSpriteGroup.update()
        self.bulletsSpriteGroup.update()

        # Handle collisions - each bullet should only resolve one enemy, once.
        bullets_to_remove = []
        enemy_hit_correct = False

        for bullet in list(self.bulletsSpriteGroup):
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemiesSpriteGroup, False)
            if not hit_enemies:
                continue

            # Only evaluate first collision per bullet to avoid duplicates
            enemy = hit_enemies[0]
            enemy_letter = enemy.name[-1]  # Get 'A', 'B', 'C', or 'D'

            if enemy_letter == self.current_correct_answer:
                print(f"{enemy.name} was hit! Correct!")
                enemy.kill()  # Remove the enemy
                enemy_hit_correct = True
            else:
                print(f"{enemy.name} was hit! Wrong, try again!")

            bullets_to_remove.append(bullet)

        # Remove bullets that hit enemies
        for bullet in bullets_to_remove:
            bullet.kill()

        # If correct hit, advance quiz and reset enemies
        if enemy_hit_correct:
            self.current_question_index += 1
            self.display_question()
            self.enemiesSpriteGroup.empty()
            self.init_enemies()
    def draw(self):
        # clear screen
        self.screen.fill(WHITE)

        self.playerSpriteGroup.draw(self.screen)
        self.enemiesSpriteGroup.draw(self.screen)
        self.bulletsSpriteGroup.draw(self.screen)

        # Draw question and answers as text centered with wrap
        y_offset = 10
        line_height = 28

        for line in self.question_text_lines:
            text_surface = self.font.render(line, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(self.SCREENWIDTH // 2, y_offset + line_height // 2))
            self.screen.blit(text_surface, text_rect)
            y_offset += line_height

        if self.current_question_index >= len(self.question_keys):
            complete_surface = self.font.render("Quiz Complete! Well done.", True, (0, 0, 0))
            complete_rect = complete_surface.get_rect(center=(self.SCREENWIDTH // 2, y_offset + 10 + line_height // 2))
            self.screen.blit(complete_surface, complete_rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

