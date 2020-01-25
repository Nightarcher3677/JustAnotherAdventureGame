import pygame
import time
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("JustAnotherAdventureGame")

pygame.mixer.music.load('button_sound.mp3')
pygame.mixer.music.load('testbeep.mp3')
rightimg = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'), pygame.image.load('4.png')]
leftimg = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png')]
button1img = pygame.image.load('button1e.png')
button2img = pygame.image.load('button2e.png')
screenwidth = 500
endlevelbutton1 = pygame.image.load('endlevelbutton1.png')
endlevelbutton2 = pygame.image.load('endlevelbutton2.png')
endlevebutton1 = pygame.image.load('endlevelbutton1left.png')
endlevebutton2 = pygame.image.load('endlevelbutton2left.png')
whiteimg = pygame.image.load('whitelight.png')
font = pygame.font.Font('freesansbold.ttf', 24)

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
level = 1
endlevelbuttondown = False
wait = True
showwhite = False

def level1():
    #pygame.mixer.music.load("level1ambience.mp3")
    #pygame.mixer.music.play(-1,0.0)
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    win.fill ((0,0,0))
    if showbutton:
        if button1edown:
            win.blit(button2img, (230, 375))
            if endlevelbuttondown:
                win.blit(endlevelbutton2, (400, 230))

                wait = True
                if wait:
                    time.sleep(0.5)
                    level = 2
            else:
                win.blit(endlevelbutton1, (400, 230))
        else:
            win.blit(button1img, (230, 375))

    font = pygame.font.Font('freesansbold.ttf', 32)
    if button1edown:
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render('Huh. I guess E interacts with stuff', True, white, black)
    else:
        text = font.render('Hello?', True, white, black)


    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)


    if y > 369 and y < 415 and x > 225 and x < 275:
        if keys[pygame.K_e] and button1edown == False:
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            button1edown = True

    if y > 220 and y < 415 and x > 265 and x < 440:
        if keys[pygame.K_e] and endlevelbuttondown == False:
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            endlevelbuttondown = True

    if x > 200 and showbutton == False:
        showbutton = True




def level2():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    if showwhite:
        text = font.render("Um. Okay...", True, white, black)
    else:
        text = font.render("That's new", True, white, black)

    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    if x < 250 and level == 2:
        showwhite = True
    elif level != 2:
        showwhite = False
    if showwhite and level == 2:
        win.blit(whiteimg, (0, 0))
    if x < 100:
        level = 3
        showwhite = False

def level3():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    showwhite = False
    win.fill ((0,0,0))
    level = 4

def level4():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    endlevelbuttondown = False
    showwhite = False
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Can't be that then.", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    win.fill ((0,0,0))
    win.blit(endlevelbutton1, (100, 100))
    if y > 90 and y < 140 and x > 90 and x < 140:
        if keys[pygame.K_e] and endlevelbuttondown == False:
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            endlevelbuttondown = True
            level = 5





def level5():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    showwhite = False
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Maybe the other direction...?", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    if level != 5:
        showwhite = False
    elif level == 5:
        win.blit(whiteimg, (0, 0))
    if x > 400:
        level = 6
        showwhite = False
        level = 6

def level6():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    endlevelbuttondown = False
    showwhite = False
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Nope!", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    win.blit(endlevebutton1, (400, 250))
    if y > 235 and y < 290 and x > 395 and x < 445:
        if keys[pygame.K_e] and endlevelbuttondown == False:
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            endlevelbuttondown = True
            level = 7

def level7():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    level = 8

def level8():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Try up?", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    if level != 8:
        showwhite = False
    elif level == 8:
        win.blit(whiteimg, (0, 0))
    if y < 100:
        level = 9
        showwhite = False
        level = 9

def level9():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    win.fill ((0,0,0))
    win.fill ((0,0,0))







def redrawgamewindow1():

    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    print(x, y)
    win.fill ((0,0,0))

    if level == 1:
        level1()
    elif level == 2:
        level2()
    elif level == 3:
        showwhite = False
        wait =  True
        endlevelbuttondown = False
        level3()
    elif level == 4:
        level4()
    elif level == 5:
        level5()
    elif level == 6:
        level6()
    elif level == 7:
        level7()
    elif level == 8:
        level8()
    elif level == 9:
        level9()

    #pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    if walkcount +1 >= 8:
        walkcount = 0

    if left:
        win.blit(leftimg[walkcount//3], (x, y))
        walkcount += 1
    else:
        win.blit(rightimg[walkcount//3], (x, y))
        walkcount += 1
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

    class projectile(object):
        def _init_(self, x , y, radius, colour, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.colour = colour
            self.facing = facing
        def draw(win):
            pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)

pygame.quit()
