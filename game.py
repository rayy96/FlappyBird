import pygame

from pygame import mixer
from pygame.locals import *

pygame.init()
mixer.init()


#set the screen
screen_width = 864
screen_height = 771


screen = pygame.display.set_mode((screen_width, screen_height),RESIZABLE)
pygame.display.set_caption("Flappy Bird")

#game variable

ground_scroll = 0
scroll_speed = 4
game_over = False
space = False
score = 0
high_score = 0
pass_pipe = False
font = pygame.font.SysFont("Bauhaus 93",60)


#Load images
background = pygame.image.load("assets/bg.png").convert_alpha()
ground = pygame.image.load("assets/ground.png").convert_alpha()

#load sound
fly_sound = pygame.mixer.Sound("assets/sound_sfx_wing.wav")
hit_sound = pygame.mixer.Sound("assets/sound_sfx_hit.wav")
point_sound= pygame.mixer.Sound("assets/sound_sfx_point.wav")
die_sound=pygame.mixer.Sound("assets/sound_sfx_die.wav")

point_sound = pygame.mixer.Sound("assets/sound_sfx_point.wav")

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(font,(x,y))







