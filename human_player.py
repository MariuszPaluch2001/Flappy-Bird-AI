import pygame
from Game import Game
def human_agent():
    pygame.init()
    window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
    clock = pygame.time.Clock()
    g = Game(1, 1)
    birds = g.get_birds()
    player_bird = birds[0]
    while True:
        clock.tick(60)
        for e in pygame.event.get():
            
            if e.type is pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    player_bird.set_moving_up()
    
        for bird in birds:
            bird.move()
            bird.falling()
            if g.colision_detection(bird):
                birds.remove(bird)
        
        g.game_iteration(window)
        if not len(birds):
            break

if __name__ == "__main__":
    human_agent()