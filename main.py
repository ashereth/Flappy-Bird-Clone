import pygame
from sys import exit
from random import randint, choice
from classes import Bird, Pipe
from variables import screen_width, screen, screen_height, sky_surface, ground_floor, ground_rect, ground_surface, clock

# pygame setup
pygame.init()
pygame.display.set_caption('Flappy')




# class and sprite group creation
bird = pygame.sprite.GroupSingle()
bird.add(Bird())
pipe = pygame.sprite.GroupSingle()
pipe = Pipe()


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, ground_rect)
    ground_rect.x-=1.5
    if ground_rect.x <= -200:
        ground_rect.x+=200

    bird.draw(screen)
    bird.update()
    screen.blit(pipe.top, pipe.top_rect)
    screen.blit(pipe.bottom, pipe.bottom_rect)
    pipe.update()
    pygame.display.update()
    clock.tick(60)