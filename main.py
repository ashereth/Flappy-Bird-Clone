import pygame
from sys import exit
from random import randint, choice
from classes import Bird, Pipe_bottom, Pipe_top
from variables import screen_width, screen, screen_height, sky_surface, ground_floor, ground_rect, ground_surface, clock, speed





# pygame setup
pygame.init()
pygame.display.set_caption('Flappy')
game_active = True


# class and sprite group creation
bird = pygame.sprite.GroupSingle()
bird.add(Bird())
pipe_group = pygame.sprite.Group()
pipe_top = Pipe_top(300)
pipe_bottom = Pipe_bottom(300)
pipe_group.add(pipe_top)
pipe_group.add(pipe_bottom ) 


# Timer for pipes
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer,3000)


def collision_sprite():
	if pygame.sprite.spritecollide(bird.sprite, pipe_group,False):#checks if player sprite is colliding with anything in the obstacle group
		pipe_group.empty()#empty obstace group so that next game starts fresh
		return False
	else: return True

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pipe_timer:
                height = randint(200, 540)
                pipe_group.add(Pipe_bottom(height), Pipe_top(height))

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, ground_rect)
        ground_rect.x-=speed
        if ground_rect.x <= -200:
            ground_rect.x+=200

        bird.draw(screen)
        bird.update()
        pipe_group.draw(screen)
        pipe_group.update()

        #game_active = collision_sprite()

    else:
         screen.fill((255, 255, 255))
    
    pygame.display.update()
    clock.tick(60)