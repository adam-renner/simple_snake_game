import pygame

class Text:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 36)
        self.score = 0
        self.color = (0, 0, 0)  # Render all text in black

    def update_score(self, increment=1):
        self.score += increment

    def render_score(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, self.color)
        screen.blit(score_text, (10, 10))
    
    def ending_text(self, line, size):
        font = pygame.font.Font(None, size)
        text = font.render(line, True, self.color)
        return text


#old version
#    def ending_text(self, message, size):
#        line_count = 0
        # font = pygame.font.Font(None, size)
        # text = font.render(message, True, self.color)
        # return text
