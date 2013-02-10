import pygame, random, time
from pygame.locals import *
from pygame.mixer import *
pygame.init()
pygame.font.init()
end = 0
easy = 0
normal = 0
hard = 0

end1 = 0

highscore1 = ""
highscore2 = ""
highscore3 = ""
highscore4 = ""
highscore5 = ""   

clock = pygame.time.Clock()
screen1 = pygame.display.set_mode((200,150),0,32)
while end == 0:
    screen1.fill((0,0,0))
    mfontz = pygame.font.SysFont("monospace", 20)
    mfonty = pygame.font.SysFont("monospace", 20)
    mfontx = pygame.font.SysFont("monospace", 20)
    fontz = mfontz.render("e = Easy", 1, (0,0,255))
    fonty = mfonty.render("n = Normal", 1, (0,0,255))
    fontx = mfontx.render("h = Hard", 1, (0,0,255))
    screen1.blit(fontz, (50,0))
    screen1.blit(fonty, (50,50))
    screen1.blit(fontx, (50,100))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                easy = 1
                end = 1
            elif event.key == pygame.K_n:
                normal = 1
                end = 1
            elif event.key == pygame.K_h:
                hard = 1
                end = 1
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    
screen = pygame.display.set_mode((800,400),0,32)
pygame.display.set_caption("Space Conquerors")

ship = pygame.image.load("images/ship.png")
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

shot = pygame.image.load("images/shot.png").convert()
shoot_y = 0

alien = pygame.image.load("images/alien.png")

explosion = pygame.image.load("images/explode.png")
pygame.transform.scale(explosion, (50,50))

score = 0
lives = 5

alien_y = 0
shoot_y = 300
alien_x = 0
alien_y1 = 0
alien_x1 = 0
alien_y2 = 0
alien_y2 = 0
num = 0
num1 = 0
num2 = 0
time = 2000

while True:

    if easy == 1:
        clock.tick(150)
    elif normal == 1:
        clock.tick(170)
    elif hard == 1:
        clock.tick(200)
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render("Score: ", 1, (0,255,0))
    myfont2 = pygame.font.SysFont("monospace", 15)
    label2 = myfont2.render(str(score), 1, (0,255,0))
    ship_width = ship.get_width()
    ship_height = ship.get_height()
    ship_y = 79
    screen.fill((0,0,0))
    screen.blit(label, (0,0))
    screen.blit(label2, (60,0))
    pygame.mouse.set_visible(0)
    x,y = pygame.mouse.get_pos()

    shoot_width = shot.get_width()
    shoot_height = shot.get_height()
    alien_width = alien.get_width()
    alien_height = alien.get_height()
    
    screen.blit(ship, (x-ship.get_width()/2,ship_top))

    shoot_x = x

    ship_x = x

    if shoot_x - alien_width < alien_x < shoot_x + shoot_width and shoot_y - alien_height < alien_y < shoot_y + shoot_height:
        if num == 0:
            alien_y = 0
            alien_x = 500
            num = 1
        elif num == 1:
            alien_y = 0
            alien_x = 300
            num = 2
        elif num == 2:
            alien_y = 0
            alien_x = 800
            num = 3
        elif num == 3:
            alien_y = 0
            alien_x = 200
            num = 0
        elif num == 4:
            alien_y = 0
            alien_x = 0
            num = 5
        elif num == 5:
            alien_y = 0
            alien_x = 600
            num = 0
        score += 100
        
    if shoot_y > -100:
        screen.blit(shot, (shoot_x, shoot_y))
        shoot_y -= 15

    screen.blit(alien, (alien_x, alien_y))
    if easy == 1:
        alien_y += 10
    elif normal == 1:
        alien_y += 15
    elif hard == 1:
        alien_y += 20
    if alien_y > 500:
        if num == 0:
            alien_y = 0
            alien_x = 500
            num = 1
        elif num == 1:
            alien_y = 0
            alien_x = 300
            num = 2
        elif num == 2:
            alien_y = 0
            alien_x = 800
            num = 3
        elif num == 3:
            alien_y = 0
            alien_x = 200
            num = 4
        elif num == 4:
            alien_y = 0
            alien_x = 0
            num = 5
        elif num == 5:
            alien_y = 0
            alien_x = 600
            num = 0
            
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            shoot_y = 300
            shoot_x = x
            pygame.mixer.Sound("sound.wav").play()

    time -= 1
    mefont = pygame.font.SysFont("monospace", 15)
    font = mefont.render("Time: ", 1, (0,255,0))
    mefont2 = pygame.font.SysFont("monospace", 15)
    font2 = mefont2.render(str(time), 1, (0,255,0))
    screen.blit(font2, (730,0))
    screen.blit(font, (680,0))
    if time == 0:
        pygame.time.delay(2000)
        pygame.quit()
        
    pygame.display.update()
