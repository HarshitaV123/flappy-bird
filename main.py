import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Flappy Bird Game")
font = pygame.font.SysFont("Times New Roman",60)
white = (255,255,255)

#define game variables
flying = False
game_over = False
pipe_gap = 150
ground_scroll = 0
scroll_speed = 4
pipe_freq = 1500
last_pipe = pygame.time.get_ticks() - pipe_freq
score = 0
pass_pipe = False

#load images
bg = pygame.image.load("images/bg.png")
ground = pygame.image.load("images/ground.png")
restart = pygame.image.load("images/restart.png")

def draw_text(text, font, white, x, y):
    txt = font.render(text, True, white)
    screen.blit(txt, (x,y))

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        
