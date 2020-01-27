import pygame
import time
import random
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init() #initialising pygame

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("JustAnotherAdventureGame")

#loading spritesheets
    #player
rightimg = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'), pygame.image.load('4.png')]
leftimg = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'), pygame.image.load('l4.png')]
    #playerattacks
rightatkimg = [pygame.image.load('atk1.png'), pygame.image.load('atk2.png'), pygame.image.load('atk3.png'), pygame.image.load('atk4.png')]
leftatkimg = [pygame.image.load('latk1.png'), pygame.image.load('latk2.png'), pygame.image.load('latk3.png'), pygame.image.load('latk4.png')]
    #enemy1
enemy1l = [pygame.image.load('enemyl1.png'), pygame.image.load('enemyl2.png'), pygame.image.load('enemyl3.png'), pygame.image.load('enemyl4.png')]
enemy1r = [pygame.image.load('enemyr1.png'), pygame.image.load('enemyr2.png'), pygame.image.load('enemyr3.png'), pygame.image.load('enemyr4.png')]

#loading buttons and stationary objects
button1img = pygame.image.load('button1e.png')
button2img = pygame.image.load('button2e.png')
endlevelbutton1 = pygame.image.load('endlevelbutton1.png')
endlevelbutton2 = pygame.image.load('endlevelbutton2.png')
endlevebutton1 = pygame.image.load('endlevelbutton1left.png')
endlevebutton2 = pygame.image.load('endlevelbutton2left.png')
buttondown1 = pygame.image.load('endlevelbuttondown1.png')
buttondown2 = pygame.image.load('endlevelbuttondown2.png')
whiteimg = pygame.image.load('whitelight.png')
pedestal = pygame.image.load('pedestal.png')
book = pygame.image.load('book.png')
fireballimg = [pygame.image.load('atk (1).png'), pygame.image.load('atk (2).png'), pygame.image.load('atk (3).png'), pygame.image.load('atk (4).png'), pygame.image.load('atk (5).png'), pygame.image.load('atk (6).png'), pygame.image.load('atk (7).png'), pygame.image.load('atk (8).png'), pygame.image.load('atk (9).png'), pygame.image.load('atk (10).png'), pygame.image.load('atk (11).png'), pygame.image.load('atk (12).png'), pygame.image.load('atk (13).png'), pygame.image.load('atk (14).png'),  pygame.image.load('atk (15).png')]
attack = False

font = pygame.font.Font('freesansbold.ttf', 24)

clock = pygame.time.Clock()
#variables
savefx = 50
savefy = 50
fx = 0
fy = 0
usedpowers = False
ex = random.randint(50, 450)
ey = random.randint(50, 450)
screenwidth = 500
x = 50.0
y = 50.0
width = 16
height = 16
vel = 5
walkcount = 0
attackcount = 0
enemycycle = 0
haspowers = False
count = 0
attackcycle = 0
left = False
stop = True
right = 0
white = (255, 255, 255)
black = (0, 0, 0)
showbutton = False
button1edown = False
level = 9
enemyhealth = 15
eVel = 2
endlevelbuttondown = False
wait = True
showwhite = False
booktaken = False
haspowers = False
first = False
shot = pygame.mixer.Sound("shot.wav")
active = False

#classes

class enemy():
    ex = random.randint(50, 450)
    ey = random.randint(50, 450)
    eVel = 1
    facing = 0
    def moveenemy():
        global facing
        global x
        global y
        global ex
        global ey
        global eVel
        global level
        global enemyhealth
        #positioning x
        if enemyhealth < 1 and level == 11:
            level = 12
        else:
            if ex > x:
                facing = -1
                if not ex - 15 < x and ( ey -15 < y or ey + 20 > y ):
                    ex -= eVel
            else:
                facing = 1
                if not ex + 30 > x and ( ey -15 < y or ey + 20 > y ):
                    ex += eVel

            #positioning y
            if ey > y:

                if not ey - 15 < y and ( ex -15 < x or ex + 45 > x ):
                    ey -= eVel
            else:

                if not ey + 45 > y and ( ex -15 < x or ex + 45 > x ):
                    ey += eVel



    def drawenemy():
        global facing
        global x
        global y
        global ex
        global ey
        global enemycycle
        if enemycycle +1 >= 8:
            enemycycle = 0

        if facing == -1:
            win.blit(enemy1l[enemycycle//3], (ex, ey))
            enemycycle += 1
        else:
            win.blit(enemy1r[enemycycle//3], (ex, ey))
            enemycycle += 1


class atk:
    def melee(damage, x, y, ex_, ey_, width, attack, offset):
        global facing
        global enemyhealth
        global ex
        global ey
        center_ex = 30 / 2 + ex_
        center_ey = 30 / 2 + ey_
        center_x = 15 / 2 + x
        center_y = 15 / 2 + y
        damage = random.randint(damage - offset, damage + offset)
        if attack:
            if facing == -1:
                if center_ex < center_x and center_ex > center_x - 50:
                        if center_ey < center_y + 15 and center_ey > center_y - 15:
                            print('damaged | ', damage)
                            enemyhealth -= damage
                            pygame.mixer.music.load('hit.wav')
                            pygame.mixer.music.play(0)
                            pygame.mixer.music.load('hit.wav')
                            pygame.mixer.music.play(0)
                            ex -= 50
            elif facing == 1:
                if center_ex > center_x and center_ex < center_x + 50:
                        if center_ey < center_y + 15 and center_ey > center_y - 15:
                            print('damaged | ', damage)
                            enemyhealth -= damage
                            pygame.mixer.music.load('hit.wav')
                            pygame.mixer.music.play(0)
                            pygame.mixer.music.load('hit.wav')
                            pygame.mixer.music.play(0)
                            ex += 50




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

    if y > 215 and y < 265 and x > 395 and x < 445:
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
    endlevelbuttondown = False
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("Ugh. How long is this going to take?", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    win.blit(buttondown1, (250, 250))
    if y > 240 and y < 290 and x > 240 and x < 300:
        if keys[pygame.K_e] and endlevelbuttondown == False:
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            endlevelbuttondown = True
            level = 10
            endlevelbuttondown = True
            showbutton = False

def level10():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    global booktaken
    global haspowers
    keys = pygame.key.get_pressed()
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("I guess we just... Press it?", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)

    if y > 100 and y < 150 and x > 230 and x < 280:
        if keys[pygame.K_e] and endlevelbuttondown:
            win.blit(buttondown1, (230, 100))
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            endlevelbuttondown = False
            showbutton = True
        elif endlevelbuttondown == False:
            win.blit(buttondown2, (230, 100))
    if endlevelbuttondown:
        win.blit(buttondown1, (230, 100))
    elif endlevelbuttondown == False:
        win.blit(buttondown2, (230, 100))


    if showbutton:
        if booktaken:
            win.blit(pedestal, (250, 250))
        else:
            win.blit(pedestal, (250, 250))
            win.blit(book, (250, 250))

        if y > 200 and y < 300 and x > 200 and x < 300:
            font = pygame.font.Font('freesansbold.ttf', 12)
            text = font.render("press E to take the book", True, white, black)
            textRect = text.get_rect()
            textRect.center = (x - 15 ,y - 20)
            win.blit(text, textRect)
            if keys[pygame.K_e]:
                pygame.mixer.music.load('take-blip.mp3')
                pygame.mixer.music.play(0)
                haspowers = True
                level = 11

def level11():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    global booktaken
    global haspowers
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render("You got magical powers! ", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    if usedpowers:
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render("Demons can only be damaged from their underside", True, white, black)
        textRect = text.get_rect()
        textRect.center = (x - 10 ,y - 20)
        win.blit(text, textRect)
    else:
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render("press SPACE to attack!", True, white, black)
        textRect = text.get_rect()
        textRect.center = (x - 10 ,y - 20)
        win.blit(text, textRect)
    enemy.moveenemy()
    enemy.drawenemy()


def level12():
    global walkcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global wait
    global endlevelbuttondown
    global showwhite
    global booktaken
    global haspowers
    win.fill ((0,0,0))
    win.fill ((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render("I think you're ready. Press the button to enter The Game", True, white, black)
    textRect = text.get_rect()
    textRect.center = (500 // 2, 75)
    win.blit(text, textRect)
    win.blit(endlevelbutton1, (100, 100))
    if y > 90 and y < 140 and x > 90 and x < 140:
        if keys[pygame.K_e] and endlevelbuttondown == False:
            pygame.mixer.music.load('button_sound.mp3')
            pygame.mixer.music.play(0)
            endlevelbuttondown = True
            level = 13


def redrawgamewindow1():
    global walkcount
    global attackcount
    global showbutton
    global button1edown
    global x
    global y
    global level
    global ey
    global facing
    global attack
    global fx
    global fy
    global first
    global usedpowers
    global haspowers
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
    elif level == 10:
        booktaken = False
        level10()
    elif level == 11:
        haspowers = True
        level11()
    elif level == 12:
        level12()




        #pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    if walkcount +1 >= 8:
        walkcount = 0

    if left:
        win.blit(leftimg[walkcount//3], (x, y))
        walkcount += 1
        facing = -1
    else:
        win.blit(rightimg[walkcount//3], (x, y))
        walkcount += 1
        facing = 1


    if keys[pygame.K_SPACE]and haspowers:
        atk.melee(5, x, y, ex, ey, 15, True, 2)
        if attackcount +1 >= 8:
            attackcount = 0
        if facing == -1:
            win.blit(leftatkimg[attackcount//3], (x - 50, y - 30))
            attackcount += 1
            if not attackcount == 4 or attackcount == 8:
                win.blit(leftatkimg[attackcount//3], (x - 50, y - 30))
                attackcount += 1
            if attackcount == 4 or attackcount == 8:
                pygame.mixer.music.load('atksound1.mp3')
                pygame.mixer.music.play(0)
        else:
            win.blit(rightatkimg[attackcount//3], (x + 15, y - 30))
            attackcount += 1
            if not attackcount == 4 or attackcount == 8:
                win.blit(rightatkimg[attackcount//3], (x + 15, y - 30))
                attackcount += 1
            if attackcount == 4 or attackcount == 8:
                pygame.mixer.music.load('atksound1.mp3')
                pygame.mixer.music.play(0)

    else:
        atk.melee(5, x, y, ex, ey, 15, False, 2)

    pygame.display.update()
'''
    if keys[pygame.K_SPACE]and haspowers:

        if left:
            if facing == -1:
                if True:#ex > x + 500 and ex < x - 10 : #and ey > y + 90 and ey < y + 65:
                    print('damaged')
            win.blit(leftatkimg[attackcount//3], (x - 50, y - 30))
            attackcount += 1
            if not attackcount == 4 or attackcount == 8:
                win.blit(leftatkimg[attackcount//3], (x - 50, y - 30))
                attackcount += 1
            if attackcount == 4 or attackcount == 8:
                pygame.mixer.music.load('atksound1.mp3')
                pygame.mixer.music.play(0)

            if attackcount +1 >= 8:
                attackcount = 0
        else:
            if facing == 1:
                if int(ex) > (x - 1) and int(ex) < (x + 100) : #and ey > y + 90 and ey < y + 65:
                    print('damaged')
            win.blit(rightatkimg[attackcount//3], (x + 15, y - 30))
            attackcount += 1
            if not attackcount == 4 or attackcount == 8:
                win.blit(rightatkimg[attackcount//3], (x + 15, y - 30))
                attackcount += 1
            if attackcount == 4 or attackcount == 8:
                pygame.mixer.music.load('atksound1.mp3')
                pygame.mixer.music.play(0)
            if attackcount +1 >= 8:
                attackcount = 0

    else:
        attackcount = 0
'''

    #pygame.display.update()


bullets = []
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
