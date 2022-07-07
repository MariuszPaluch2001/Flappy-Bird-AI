import pygame

class Block:
    """
    Blocks are part of pipe. That give me oportunity for
    creating proper texture for pipe.
    """
    WIDTH = 30
    HEIGHT = 50
    IMAGE = pygame.transform.scale(pygame.image.load("assets/pipe_bottom.png"), (WIDTH, HEIGHT))
    def __init__(self, x_position, y_position) -> None:
        self.x = x_position
        self.y = y_position
    
    def draw(self, surface):
        surface.blit(self.IMAGE , (self.x, self.y))

    def move(self, velocity : float):
        self.x -= velocity
        
class End_Block_Upper(Block):

    IMAGE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pipe_upper.png"), (Block.WIDTH, Block.HEIGHT)), 180)
    def __init__(self, x_position: float, y_position: float) -> None:
        super().__init__(x_position, y_position)

class End_Block_Down(Block):
    
    IMAGE = pygame.transform.scale(pygame.image.load("assets/pipe_upper.png"), (Block.WIDTH, Block.HEIGHT))
    def __init__(self, x_position, y_position) -> None:
        super().__init__(x_position, y_position)

class Pipe:
    """
    Pipe is composed of blocks.
    """
    def __init__(self, x_position, y_position, blocks_number) -> None:
        self.x = x_position
        self.y = y_position
        self.blocks_number = blocks_number
        self.pipe_blocks = self._blocks_creation()
        self.is_passed = False
        
    def _blocks_creation(self):
        blocks = [Block(self.x, self.y + i * Block.HEIGHT) for i in range(self.blocks_number)]
        blocks.append(End_Block_Upper(self.x, self.y + self.blocks_number * Block.HEIGHT))
        
        return blocks

    def move(self, velocity):
        self.x -= velocity
        for block in self.pipe_blocks:
            block.move(velocity)

    def draw(self, surface):
        for block in self.pipe_blocks:
            block.draw(surface)

class Pipe_Down(Pipe):
    def __init__(self, x_position, y_position, blocks_number) -> None:
        super().__init__(x_position, y_position, blocks_number)

    def _blocks_creation(self):
        blocks = [Block(self.x, self.y + i * Block.HEIGHT) for i in range(self.blocks_number)]
        blocks.append(End_Block_Down(self.x, self.y))

        return blocks