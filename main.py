import pygame


clock = pygame.time.Clock()

pygame.init()


screen = pygame.display.set_mode((920, 518))
pygame.display.set_caption("Angry birds [github.com/colibrimp]")
icon = pygame.image.load("img/game_birds_icon.png")

# icon
pygame.display.set_icon(icon)



bg_img = pygame.image.load("images/Forest.jpg").convert_alpha()


#Player
movement_left = [
    pygame.image.load("images/ab_left/ab_left.png").convert_alpha(),
    pygame.image.load("images/ab_left/ab_left2.png").convert_alpha(),
    pygame.image.load("images/ab_left/ab_left3.png").convert_alpha(),
]

movement_right = [
    pygame.image.load("images/ab_right/angry_birds_left.png").convert_alpha(),
    pygame.image.load("images/ab_right/angry_birds_left1.png").convert_alpha(),
    pygame.image.load("images/ab_right/angry_birds_left2.png").convert_alpha(),
    pygame.image.load("images/ab_right/angry_birds_left3.png").convert_alpha(),
]

monster_img = pygame.image.load("images/venonat.png").convert_alpha()
monster_x = 920


player_movement_index = 0
bg_move = 0

speed_player = 5

player_x = 150
player_y = 250

player_jump = False
jump_count = 10


# sound game
sound_cage = pygame.mixer.Sound("sounds/calambur.mp3")
sound_cage.play()

running = True

while running:


    screen.blit(bg_img, (bg_move, 0))
    screen.blit(bg_img, (bg_move + 920, 0))

    screen.blit(monster_img, (monster_x, 250))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(movement_left[player_movement_index], (player_x, player_y))
    else:
        screen.blit(movement_right[player_movement_index], (player_x, player_y))



    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= speed_player
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += speed_player
        
    # jump player
    if not player_jump:
        if keys[pygame.K_SPACE]:
            player_jump = True
    else:
        if jump_count >= -10:
            player_y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else:
            if jump_count >= -10:
                if jump_count < 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                player_jump = False
                jump_count = 10




    if player_movement_index == 3:
        player_movement_index = 0
    else:
        player_movement_index += 1


    bg_move -= 8
    if bg_move == -920:
        bg_move = 0

    monster_x -= 10


    pygame.display.update()

    #button exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(8)
