import pygame, sys

pygame.init()

VEL = 5

health_font = pygame.font.SysFont("comicsans", 40)

HEIGHT, WIDTH = 500,900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invasion")
screen.fill("white")

border = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) 

space2 = pygame.transform.scale(pygame.image.load("space2.png"), (WIDTH, HEIGHT))

sw, sh = 55, 40
yellow_player = pygame.transform.scale(pygame.image.load("yellow_player.png"), (sw, sh))
red_player = pygame.transform.scale(pygame.image.load("red_player.png"), (sw, sh))

yellow_rotated = pygame.transform.rotate(yellow_player, 90)
red_rotated = pygame.transform.rotate(red_player, 270)

pygame.display.update()

def draw(yellow, red, red_health, yellow_health):
    screen.blit(space2, (0,0))

    red_text = health_font.render("Health:" + str(red_health), 1, "white")
    yellow_text = health_font.render("Health:" + str(yellow_health), 1, "white")

    pygame.draw.rect(screen, "white", border)
    screen.blit(yellow_rotated, (yellow.x, yellow.y))
    screen.blit(red_rotated, (red.x, red.y))
    screen.blit(red_text, (WIDTH - red_text.get_width() - 10, 10))
    screen.blit(yellow_text, (10, 10))

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VEL

#right = plus, up = plus, down = minus

while True:

    yellow = pygame.Rect(100, 300, sw, sh)
    red = pygame.Rect(700, 300, sw, sh)

    red_health = 10
    yellow_health = 10

    keys_pressed = pygame.key.get_pressed()
    yellow_handle_movement(keys_pressed, yellow)

    draw(yellow, red, red_health, yellow_health)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()