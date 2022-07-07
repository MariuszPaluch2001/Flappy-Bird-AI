from Ground import Ground
from Bird import Bird
from Pipe import Block, Pipe, Pipe_Down
import time
import random
import pygame
class Game:
    WIDTH = 400
    HEIGHT = 700
    BIRDS_START_POSITION = (50,50)
    BREAK_SIZE = Block.HEIGHT*2
    RANGE_PIPE = (1, HEIGHT // Block.HEIGHT - 6)
    SKY_BLUE = (135, 206, 235)
    def __init__(self, birds_number, pipes_velocity) -> None:
        self.ground = Ground(0, Game.HEIGHT - Ground.HEIGHT, Game.WIDTH)
        self.pipes = []
        self.add_new_pipe()
        self.pipes_velocity = pipes_velocity
        self.birds_number = birds_number
        self.birds = self.birds_create()
        self.score = 0

    def birds_create(self):
        return [Bird(self.BIRDS_START_POSITION[0], self.BIRDS_START_POSITION[1]) for _ in range(self.birds_number)]

    def pipe_create(self):
        if len(self.pipes) < 4 and self.pipes[0].x < self.BIRDS_START_POSITION[0]:
            self.add_new_pipe()

    def add_new_pipe(self):
        rand_pipe_len = random.randint(self.RANGE_PIPE[0],  self.RANGE_PIPE[1])
        self.pipes.append(Pipe(self.WIDTH, 0,rand_pipe_len))
        self.pipes.append(Pipe_Down(self.WIDTH, (rand_pipe_len + 1)* Block.HEIGHT + self.BREAK_SIZE, 9 - rand_pipe_len))
    
    def draw(self, surface):
        surface.fill(self.SKY_BLUE)
        self.ground.draw(surface)
        for bird in self.birds:
            bird.draw(surface)
        for pipe in self.pipes:
            pipe.draw(surface)
        pygame.display.flip()
    
    def pipe_move(self):
        for pipe in self.pipes:
            pipe.move(self.pipes_velocity)

    def destroy(self):
        if len(self.pipes) > 1 and self.pipes[0].x < - Block.WIDTH:
            for _ in range(2):
                self.pipes.remove(self.pipes[0])
    
    def colision_detection(self, bird):
        if bird.y + Bird.BIRD_SIZE > self.HEIGHT - Ground.HEIGHT:
                return True
            
        if len(self.pipes) > 1:
            if self.pipes[0].x - bird.BIRD_SIZE < bird.x < self.pipes[0].x + Bird.BIRD_SIZE:
                if self.pipes[0].y + Block.HEIGHT * (self.pipes[0].blocks_number + 1)  > bird.y:
                    return True
                    
                if bird.y + Bird.BIRD_SIZE > self.pipes[1].y:
                    return True
            
        return False

    def passing(self, bird):
        if len(self.pipes) > 1 and not self.pipes[0].is_passed and self.pipes[0].x + Block.WIDTH < bird.x:
            self.pipes[0].is_passed = True
            self.score += 1
            print(f"New score: {self.score}")
            return True
        
        return False

    def game_iteration(self, surface):
        self.pipe_create()
        self.pipe_move()
        self.draw(surface)

        # for bird in self.birds:
        #     bird.falling()
        self.destroy()
        # if self.colision_detection():
        #     return False

    def game_restart(self):
        self.pipes = []
        self.time_stamp = time.time()
        self.birds = self.birds_create()

    def get_birds(self):
        return self.birds

    def get_pipe_up_x(self):
        if len(self.pipes) > 1:
            return self.pipes[0].y

    def get_pipe_down_x(self):
        if len(self.pipes) > 1:
            return self.pipes[1].y

