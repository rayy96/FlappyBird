import sys

import pygame
from pygame.examples.aliens import Score

import game
import pipes
from bird import *
from pipes import *
from pygame import *
from pygame.locals import *
import random




pygame.init()

clock = pygame.time.Clock()
fps = 60
game_font = pygame.font.Font('04B_19.ttf',40)
game_state = False


#bird groups
bird_groups = pygame.sprite.Group()
flappy = bird(100,int(game.screen_height)/2)
bird_groups.add(flappy)


#pipes groups
pipes_groups = pygame.sprite.Group()

# score display
def score_display(game_state):

  if game_state == False:

        score_surface = game_font.render(str(int(game.score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(432, 100))
        game.screen.blit(score_surface, score_rect)

  if game_state == True:

        score_surface = game_font.render(f'Score: {int(game.score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(432, 70))
        game.screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(game.high_score)}', True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center=(390, 700))
        game.screen.blit(high_score_surface, high_score_rect)
        game.screen.blit(game.game_over_surface, game.game_over_rect)



def update_score():
    if game.score > game.high_score:
        game.high_score = game.score
    return game.high_score

def rotate_bird(image):
        new_bird = pygame.transform.rotozoom(bird.image, bird.movement * 3, 1)
        return new_bird

run = True
while run:



    clock.tick(fps)
    #we get the size of the screen
    image_w = game.screen.get_width()
    image_h = game.screen.get_height()

    #we scalling images
    image_ground = pygame.transform.scale(game.ground, (image_w, ((game.ground.get_height()*168))/313))
    image_background = pygame.transform.scale(game.background, (image_w, (image_h-image_ground.get_height())))

    # draw the Background
    game.screen.blit(image_background, (0,0))

    # draw birds
    bird_groups.draw(game.screen)
    bird_groups.update(bird.hitSomething)

    # draw pipes
    pipes_groups.draw(game.screen)



    #draw the ground
    game.screen.blit(image_ground, (game.ground_scroll, image_background.get_height()))

    if game.game_over == False and bird.flying == True:

        #create new pipe
        time_now = pygame.time.get_ticks()
        if time_now - pipes.last_pipe > pipes.pipes_frequency:
            # pipes groups
            pipes_height = random.randint(-100,100)
            bottom_pipes = pipes(game.screen_width-1, int(game.screen_height / 2)+pipes_height, -1)
            up_pipes = pipes(game.screen_width-1, int(game.screen_height / 2+pipes_height), 1)
            pipes_groups.add(bottom_pipes)
            pipes_groups.add(up_pipes)
            pipes.last_pipe = time_now

        #check the score
        if len(pipes_groups)>0:
            if bird_groups.sprites()[0].rect.left > pipes_groups.sprites()[0].rect.left\
            and bird_groups.sprites()[0].rect.right < pipes_groups.sprites()[0].rect.right\
            and game.pass_pipe == False :

                game.pass_pipe = True
        if game.pass_pipe == True:
            if bird_groups.sprites()[0].rect.left > pipes_groups.sprites()[0].rect.right:
              game.score +=1
              pygame.mixer.Sound.play(game.point_sound)
              game.pass_pipe =False

        #scroll the ground
        game.ground_scroll -= game.scroll_speed
        if abs(game.ground_scroll)>35:
            game.ground_scroll = 0

        #update the pipes
        pipes_groups.update()

    #check if there is collision
    if pygame.sprite.groupcollide(bird_groups,pipes_groups,False,False) or flappy.rect.top < 0:
        game.game_over = True
        game.high_score = update_score()
        score_display(True)

        # Score display
        if not bird.hitSomething :
            pygame.mixer.Sound.play(game.hit_sound)
            bird.hitSomething = True

    else:
        score_display(False)


    #check if bird had hit the ground
    if flappy.rect.bottom > image_background.get_height():
        game.game_over = True
        bird.flying = False
        bird.hitTheGround = True

        # rotete bird
        rotated_bird = bird.rotate_bird()




    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and bird.flying==False and game.game_over == False:
            bird.flying = True

        if event.type == pygame.MOUSEBUTTONDOWN and bird.flying==False and game.game_over == True:
            game.game_over == False


    pygame.display.update()


pygame.QUIT
