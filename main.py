import pygame
from sys import exit
from random import randint, choice
from classes import Bird, Pipe_bottom, Pipe_top
from variables import screen_width, screen, screen_height, sky_surface, ground_floor, ground_rect, ground_surface, clock, speed





# pygame setup
pygame.init()
pygame.display.set_caption('Flappy')
test_font = pygame.font.Font('font/Pixeltype.ttf', 80)
game_active = False
score = 0

# Menu Screen setup
game_name = test_font.render('Flappy Guy',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (screen_width//2,80))
menu_bird_surf = pygame.image.load('graphics/bird/flappy.png').convert_alpha()
menu_bird_rect = menu_bird_surf.get_rect(center = (screen_width//2, screen_height//2-100))
game_message = test_font.render('Press space to start',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (screen_width//2,450))

# class and sprite group creation
bird = pygame.sprite.GroupSingle()
bird.add(Bird())
pipe_group = pygame.sprite.Group()
pipe_top = Pipe_top(300)
pipe_bottom = Pipe_bottom(300)
pipe_group.add(pipe_top)
pipe_group.add(pipe_bottom ) 
all_sprites = pygame.sprite.Group()
all_sprites.add(pipe_bottom, pipe_top, bird)

# Timer for spawning pipes
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer,3000)


#function for determining if the bird is colliding with any pipes
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
        # for spawning new pipes 
        if game_active:
            if event.type == pipe_timer:
                height = randint(240, 550)
                pipe_group.add(Pipe_bottom(height), Pipe_top(height))
        else: # start the game if spacebar is pressed and game is not active
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score = 0

    if game_active:
        # draw the ground, sky, and score making sure to render a new score every frame to keep it updated
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface, ground_rect)
        score_surf = test_font.render(f'{score}',False,"black")
        score_rect = score_surf.get_rect(center = (screen_width//2+10,50))
        
        #move ground to the left and if it goes too far reset it so that it can loop forever
        ground_rect.x-=speed
        if ground_rect.x <= -200:
            ground_rect.x+=200

        #draw the bird and pipes
        bird.draw(screen)
        bird.update()
        pipe_group.draw(screen)
        pipe_group.update()
        #draw the score on top of everything
        screen.blit(score_surf, score_rect)
        #update score whenever a pipe passes through bird
        for pipe in pipe_group:
             if pipe.rect.x == 270:
                  score+= 1

        # check for collisions and update game_active
        game_active = collision_sprite()

    else:# if game is not active show a basic menu screen
        screen.fill((94,129,162))
        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        screen.blit(menu_bird_surf, menu_bird_rect)
        score_message_rect = score_message.get_rect(center = (screen_width//2,330))
        screen.blit(game_name,game_name_rect)
        # if the last score was 0 print a message otherwise print the last score
        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message,score_message_rect)
    
    pygame.display.update()
    clock.tick(60)