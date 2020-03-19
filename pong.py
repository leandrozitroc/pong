import sys, pygame
from paddle import Paddle
from ball import Ball
pygame.init()
yellow = (255,190,0)
blue = (255,190,210)

clock = pygame.time.Clock()
size = width, height = 600, 400
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Slitter')
ball = Ball(yellow,10,10)
ball.rect.x = 345
ball.rect.y = 195

score_A = 0
score_B = 0
paddleA = Paddle(yellow, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(blue, 10, 100)
paddleB.rect.x = 570
paddleB.rect.y = 200
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if ball.rect.x >= 580:
        ball.velocity[0] = -ball.velocity[0]
        score_A += 1
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        score_B +=1
    if ball.rect.y > 380:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddleA.moveup(5)
    if keys[pygame.K_DOWN]:
        paddleA.movedown(5)
    if keys[pygame.K_q]:
        paddleB.moveup(5)
    if keys[pygame.K_a]:
        paddleB.movedown(5)

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    all_sprites_list.update()
    all_sprites_list.draw(screen)
    placar = pygame.draw.rect(screen, (96, 96, 96), (200, 10, 150, 80))
    letreito = pygame.font.Font(None, 40)
    text = letreito.render('Placar', 1, (0,102,0))
    screen.blit(text, (235,10))
    linha1 = pygame.draw.line(screen, (0,0,0), (275,45),(275,90), width=3)
    linha2 = pygame.draw.line(screen, (0,0,0), (200,45),(350,45), width=3)
    font = pygame.font.Font(None, 50)
    text = font.render(str(score_A), 1,yellow)
    screen.blit(text, (225, 50))
    font = pygame.font.Font(None, 50)
    text = font.render(str(score_B), 1, yellow )
    screen.blit(text, (305, 50))


    pygame.display.flip()

    screen.fill(black)
    clock.tick(60)
