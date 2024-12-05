import pygame, sys

pygame.init()

yellow_hit = pygame.USEREVENT + 1 #pygame.USEREVENT = 24th event out of 32
red_hit = pygame.USEREVENT + 2 #26th event

VEL = 5
bullet_velocity = 7

health_font = pygame.font.SysFont("comicsans", 40)
winner_font = pygame.font.SysFont("comicsans", 100)

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

def draw(yellow, red, red_health, yellow_health, red_bullets, yellow_bullets):
    screen.blit(space2, (0,0))

    red_text = health_font.render("Health:" + str(red_health), 1, "white")
    yellow_text = health_font.render("Health:" + str(yellow_health), 1, "white")

    pygame.draw.rect(screen, "white", border)
    screen.blit(yellow_rotated, (yellow.x, yellow.y))
    screen.blit(red_rotated, (red.x, red.y))
    screen.blit(red_text, (WIDTH - red_text.get_width() - 10, 10))
    screen.blit(yellow_text, (10, 10))

    for bullet in red_bullets:
        pygame.draw.rect(screen, "red", bullet)


    for bullet in yellow_bullets:
        pygame.draw.rect(screen, "yellow", bullet)


    pygame.display.update()

#yellow key movements

#left
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VEL

#right
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width < border.x:
        yellow.x += VEL

#up
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= VEL

#down
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height < HEIGHT:
        yellow.y += VEL

#red key movements

#left
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > border.x + border.width:
        red.x -= VEL

#right
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width < WIDTH:
        red.x += VEL

#up
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= VEL

#down
    if keys_pressed[pygame.K_DOWN]and red.y + red.height < HEIGHT:
        red.y += VEL

def handle_bullets(yellow_bullets, red_bullets, red, yellow):
    for bullet in yellow_bullets:
        bullet.x += bullet_velocity
        if red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            print("working")
            pygame.event.post(pygame.event.Event(red_hit))
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_velocity
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(yellow_hit))
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(txt):
    draw_text = winner_font.render(txt, 1, "white")
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    yellow = pygame.Rect(100, 300, sw, sh)
    red = pygame.Rect(700, 300, sw, sh)

    red_bullets = []
    yellow_bullets= []

    max_bullet = 3

    red_health = 10
    yellow_health = 10

    run = True

    while run:

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, red, yellow)
        draw(yellow, red, red_health, yellow_health, red_bullets, yellow_bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets) < max_bullet:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2-2, 10, 5)
                    yellow_bullets.append(bullet)
                
                if event.key == pygame.K_RSHIFT and len(red_bullets) < max_bullet:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2+2, 10, 5)
                    red_bullets.append(bullet)

            if event.type == red_hit:
                red_health -= 1

            if event.type == yellow_hit:
                yellow_health -= 1
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "yellow wins!!"
        if yellow_health <=0:
            winner_text = "red wins!!"
        if winner_text != "":
            draw_winner(winner_text)
            break

    main()

if __name__ == "__main__":
    main()


