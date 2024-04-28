import pygame


clock = pygame.time.Clock()
FPS = 10
pygame.init()


screen = pygame.display.set_mode((920, 518))
pygame.display.set_caption("Angry birds [github.com/colibrimp]")
icon = pygame.image.load("images/birds_icon.png").convert_alpha()

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

# Monster
monster_img = pygame.image.load("images/venonat.png").convert_alpha()
monster_x = 920
monster_y = 280

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

# Timer for monster
monster_timer = pygame.USEREVENT + 1
pygame.time.set_timer(monster_timer, 3000)


monster_list = []

running = True

while running:
    screen.blit(bg_img, (bg_move, 0))
    screen.blit(bg_img, (bg_move + 920, 0))

    player_rect = movement_left[0].get_rect(topleft=(player_x, player_y))

    if monster_list:
            for monst in monster_list:
              # draw monster
                screen.blit(monster_img, monst)
                monst.x -= 10

               # contact between player and monster
                if player_rect.colliderect(monst):
                    print("Game over")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and pygame.KEYDOWN:
        screen.blit(movement_left[player_movement_index], (player_x, player_y))
    else:
        screen.blit(movement_right[player_movement_index], (player_x, player_y))

    
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed_player
    elif keys[pygame.K_RIGHT] and player_x < 920:
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

         # add monster
        if event.type == monster_timer:
            monster_list.append(monster_img.get_rect(topleft=(920, 300)))

    clock.tick(FPS)
