import pygame.sprite
import pygame

import game

class pipes(pygame.sprite.Sprite):
    pipe_gap = 200
    pipes_frequency = 2000
    last_pipe = pygame.time.get_ticks()


    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/pipe.png').convert_alpha()
        self.rect = self.image.get_rect()
        #position 1 is from top and -1 from bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-int(pipes.pipe_gap/2)]
        if position == -1:
            self.rect.topleft = [x,y+int(pipes.pipe_gap/2)]

    def update(self):
        self.rect.x -= game.scroll_speed
        if self.rect.right <0:
            self.kill()

