import pygame
from sys import exit
from random import randint, choice

# basic variables and pygame setup
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy')
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_1 = pygame.image.load('graphics/bird/flappy.png').convert_alpha()
        bird_1 = pygame.transform.rotozoom(bird_1, 0, 3)
        self.moving = [bird_1]
        self.index = 0
        self.image = self.moving[self.index]
        self.rect = self.image.get_rect(midbottom = (screen_width//2, 300))
        self.gravity = 0



# class and sprite group creation
bird = pygame.sprite.GroupSingle()
bird.add(Bird())


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    bird.draw(screen)

    pygame.display.update()
    clock.tick(60)