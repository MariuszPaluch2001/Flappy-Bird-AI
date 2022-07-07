import pygame

class Bird:
    UP_VELOCITY = 15
    FALLING_BIRD = 2.5
    BIRD_SIZE = 30
    IMAGE = pygame.transform.scale(pygame.image.load("assets/bird.png"), (BIRD_SIZE, BIRD_SIZE))
    FLYING_ITER = 3
    def __init__(self, x_position, y_position) -> None:
        self.x = x_position
        self.y = y_position
        self.counter_flying = 0

    def draw(self, surface):
        surface.blit(self.IMAGE , (self.x, self.y))

    def move(self):
        if self.counter_flying > 0:
            self.y -= self.UP_VELOCITY
            self.counter_flying -= 1

    def falling(self):
        self.y += self.FALLING_BIRD

    def set_moving_up(self):
        self.counter_flying = self.FLYING_ITER