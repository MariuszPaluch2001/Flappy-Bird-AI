import os
import neat
import pygame
from Game import Game
import pickle

def AI_agent(genomes, config):
    pygame.init()
    window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
    clock = pygame.time.Clock()
    game = Game(len(genomes), 1)

    nets = []
    ge = []
    birds = game.get_birds()
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)

    while True:
        for e in pygame.event.get():
            
            if e.type is pygame.QUIT:
                quit()


        game.game_iteration(window)

        for index, bird in enumerate(birds):
            bird.move()
            bird.falling()
            ge[index].fitness += 0.1
            output = nets[index].activate((bird.y, abs(bird.y - game.get_pipe_up_x()), abs(bird.y - game.get_pipe_down_x())))

            if output[0] > 0.5:
                bird.set_moving_up()
            if game.colision_detection(bird):
                ge[index].fitness -= 1
                birds.pop(index)
                nets.pop(index)
                ge.pop(index)

            if game.passing(bird):
                ge[index].fitness += 5
        
        if game.score > 20:
            pickle.dump(nets[0],open("best.pickle", "wb"))
            break
        if not len(birds):
            break

def run(config_path):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(AI_agent, 1000)

    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)