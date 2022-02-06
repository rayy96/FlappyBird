import pygame

import pygame
from pygame import *

import game


class bird(pygame.sprite.Sprite):
    flying = False
    hitSomething = False
    def __init__(bird, x, y):
        pygame.sprite.Sprite.__init__(bird)
        bird.images = []
        bird.index = 0
        bird.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'assets/bird{num}.png').convert_alpha()
            bird.images.append(img)
        bird.image= bird.images[bird.index]
        bird.rect = bird.image.get_rect()
        bird.rect.center = [x, y]
        bird.movement = 0
        bird.clicked = False


    def update(bird, hitSomething=hitSomething):
        if bird.flying == True:
            #gravity
            bird.movement += 0.5
            if bird.movement >8:
                bird.movement = 8
            if bird.rect.bottom < 681:
                bird.rect.y += int(bird.movement)


        if hitSomething == False:
            #jump
            if pygame.mouse.get_pressed()[0]==1  and  bird.clicked == False:
                bird.clicked = True
                bird.movement = -5
                pygame.mixer.Sound.play(game.fly_sound)
            if pygame.mouse.get_pressed()[0] == 0:
                bird.clicked = False

            #handle the animation
            bird.counter += 1
            limit = 5

            if bird.counter > limit:
                bird.counter = 0
                bird.index +=1
                if bird.index >= len(bird.images):
                    bird.index = 0
            bird.image = bird.images[bird.index]





            #rotate the bird

        #else :
            #bird.image = pygame.transform.rotate(bird.images[bird.index], -90)



