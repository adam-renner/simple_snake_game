import random

class Pellet:
    def __init__(self, width, height, snake_body):
        self.width = width
        self.height = height
        self.snake_body = snake_body
        self.position = self.get_random_position()

    def get_random_position(self):
        while True:
            position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if position not in self.snake_body:
                return position

    def move(self, snake_position):
        self.snake_body = snake_position
        self.position = self.get_random_position()

    def check_collision(self, snake_head):
        if self.position == snake_head:
            return True
        return False
