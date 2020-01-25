import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("JustAnotherAdventureGame")

rightimg = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'), pygame.image.load('4.png')]
leftimg = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png')]
button1img = pygame.image.load('button1e.png')
button2img = pygame.image.load('button2e.png')
screenwidth = 500

clock = pygame.time.Clock()
x = 50
y = 50
width = 16
height = 16
vel = 5
walkcount = 0
left = False
right = 0
white = (255, 255, 255)
black = (0, 0, 0)
showbutton = False
button1edown = False

def redrawgamewindow1():
    global walkcount
    global showbutton
    global button1edown
    win.fill ((0,0,0))
    if showbutton:
        if button1edown:
            win.blit(button2img, (230, 375))
        else:
            win.blit(button1img, (230, 375))

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Hello?', True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)

    if walkcount +1 >= 8:
        walkcount = 0

    if left:
        win.blit(leftimg[walkcount//3], (x, y))
        walkcount += 1
    else:
        win.blit(rightimg[walkcount//3], (x, y))
        walkcount += 1

    if x > 280:
        showbutton = True


    #pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()



run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        right = 0
        left = True
    if keys[pygame.K_RIGHT] and x < screenwidth - width:
        x += vel
        right = 1
        left = False
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN]and y < screenwidth - height - vel:
        y += vel

    redrawgamewindow1()



pygame.quit()