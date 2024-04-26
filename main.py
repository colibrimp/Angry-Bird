import pygame


clock = pygame.time.Clock()

pygame.init()


screen = pygame.display.set_mode((920, 518))
pygame.display.set_caption("Angry birds [github.com/colibrimp]")
icon = pygame.image.load("img/game_birds_icon.png")

pygame.display.set_icon(icon)

screen.fill((52, 235, 229))


bg_img = pygame.image.load("images/Forest.jpg")


movement = [
    pygame.image.load("images/angry_birds_left.png"),
    pygame.image.load("images/angry_birds_left1.png"),
    pygame.image.load("images/angry_birds_left2.png"),
    pygame.image.load("images/angry_birds_left3.png"),
]

movement_index = 0
bg_move = 0

# sound game
sound_cage = pygame.mixer.Sound("sounds/calambur.mp3")
sound_cage.play()

running = True

while running:

    screen.blit(bg_img, (bg_move, 0))
    screen.blit(bg_img, (bg_move + 920, 0))
    screen.blit(movement[movement_index], (100, 320))

    if movement_index == 3:
        movement_index = 0
    else:
        movement_index += 1


    bg_move -= 8
    if bg_move == -920:
        bg_move = 0

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(8)
