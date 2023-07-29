import pygame
import sys
from objects.snake import Snake
from objects.pellet import Pellet
from objects.text import Text
from objects.grid import Grid


class GameHandler:
    def __init__(self, cells, cell_size=50):
        pygame.init()
        self.cells = cells
        self.cell_size = cell_size
        width = len(cells[0])
        height = len(cells)
        self.snake = Snake(width, height,)
        self.pellet = Pellet(width, height, self.snake.positions)
        self.text = Text()
        self.grid = Grid(width, height)
        self.screen = self.screen = pygame.display.set_mode((width*cell_size, height*cell_size))

    def draw_cell(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))

    def display(self):
        # Render the game, including the snake, pellets, and score display
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell == "snake":
                    self.draw_cell(j, i, (0, 255, 0))  # Draw a green cell for the snake
                elif cell == "food":
                    self.draw_cell(j, i, (255, 0, 0))  # Draw a red cell for food
                else:
                    self.draw_cell(j, i, (255, 255, 255))  # Draw a white cell for empty space
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(10)  # Limit the frame rate to 10 frames per second
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.handle_input()
            game_over = self.update()
            if game_over:
                self.game_over()
            else:
                self.display()
            self.text.render_score(self.screen)
            pygame.display.flip()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.snake.change_direction((-1, 0))  # Move left
        elif keys[pygame.K_RIGHT]:
            self.snake.change_direction((1, 0))  # Move right
        elif keys[pygame.K_UP]:
            self.snake.change_direction((0, -1))  # Move up
        elif keys[pygame.K_DOWN]:
            self.snake.change_direction((0, 1))  # Move down


    def update(self):
    # Reset cells to empty state
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.cells[i][j] = None

        self.snake.move(len(self.cells[0]), len(self.cells))
        if self.pellet.check_collision(self.snake.positions[0]):
            self.snake.grow()
            self.text.update_score()
            self.pellet.move(self.snake.positions)

        # Mark snake cells
        for position in self.snake.positions:
            x, y = position
            if 0 <= x < len(self.cells[0]) and 0 <= y < len(self.cells):
                self.cells[y][x] = "snake"
            else:
                return True # Game over if snake is out of the grid

        # Mark pellet cell
        pellet_x, pellet_y = self.pellet.position
        if 0 <= pellet_x < len(self.cells[0]) and 0 <= pellet_y < len(self.cells):
            self.cells[pellet_y][pellet_x] = "food"

        if self.snake.check_collision(len(self.cells[0]), len(self.cells)):
            return True # Game over if snake collides with itself
        
        return False # Game continues otherwise

    def game_over(self):
        lines = ["Game Over", "Press R to restart", "Press Q to quit", "Thanks for playing! :)"]
        next_line = self.screen.get_height() // 2 - len(lines) * 10  # Adjust this value as needed

        for index, line in enumerate(lines):
            if index == 0:
                size = 50
            else:
                size = 30
            text = self.text.ending_text(line, size)  # 30 is the font size
            rect = text.get_rect()
            rect.center = (self.screen.get_width() // 2, next_line)
            self.screen.blit(text, rect)
            next_line += rect.height + 10  # 10 is the space between lines

        pygame.display.flip()
    
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Press 'r' key to restart the game
                        self.__init__(self.cells, self.cell_size)
                        self.run()
                    elif event.key == pygame.K_q:  # Press 'q' key to quit the game
                        pygame.quit()
                        sys.exit()
            pygame.time.wait(10)  # Wait for a while to reduce the CPU load
        
