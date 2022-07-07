import pygame

class Ground:
    FILLING = (126, 200, 80)
    HEIGHT = 100
    def __init__(self, x_position, y_position, width) -> None:
        self.x = x_position
        self.y = y_position
        self.width = width

    def draw(self, surface):
        pygame.draw.rect(surface, self.FILLING, pygame.Rect(self.x, self.y, self.width, self.HEIGHT))