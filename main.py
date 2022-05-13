import pygame, sys
from level import Level
from settings import *
from tile import Coin

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Champ')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.font = pygame.font.SysFont('Comic Sans Ms', 32)

        #self.text = self.font.render('Score = ' + str(self.score), True,(0,255,0))
        #self.textRect = self.text.get_rect()
        #self.textRect.center = (100,40)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('gray')
            # debug('hello :)')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
