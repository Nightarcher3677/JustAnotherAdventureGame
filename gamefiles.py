import pygame
import time
import random
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.key.set_repeat(1)
#loading images
bg = pygame.image.load('floor_10.png')
enemy1l = [pygame.image.load('enemyl1.png'), pygame.image.load('enemyl2.png'), pygame.image.load('enemyl3.png'), pygame.image.load('enemyl4.png')]
enemy1r = [pygame.image.load('enemyr1.png'), pygame.image.load('enemyr2.png'), pygame.image.load('enemyr3.png'), pygame.image.load('enemyr4.png')]

#hp images
hp00 = pygame.image.load('hp-00.png')
hp01 = pygame.image.load('hp-01.png')
hp02 = pygame.image.load('hp-02.png')
hp03 = pygame.image.load('hp-03.png')
hp04 = pygame.image.load('hp-04.png')
hp05 = pygame.image.load('hp-05.png')
hp06 = pygame.image.load('hp-06.png')
hp07 = pygame.image.load('hp-07.png')
hp08 = pygame.image.load('hp-08.png')
hp09 = pygame.image.load('hp-09.png')
hp10 = pygame.image.load('hp-10.png')
hp11 = pygame.image.load('hp-11.png')
hp12 = pygame.image.load('hp-12.png')
hp13 = pygame.image.load('hp-13.png')
hp14 = pygame.image.load('hp-14.png')
hp15 = pygame.image.load('hp-15.png')
hp16 = pygame.image.load('hp-16.png')
hp17 = pygame.image.load('hp-17.png')
hp18 = pygame.image.load('hp-18.png')

#button images
button1 = pygame.image.load('button1.png')
button2 = pygame.image.load('button2.png')

escup = pygame.image.load('esc-up.png')
escdown = pygame.image.load('esc-down.png')

#weapon images
    #legendaries
L1 = pygame.image.load('legendaries\1.png')
L2 = pygame.image.load('legendaries\2.png')
    #common
C1 = pygame.image.load('common\1.png')

menu = True
Pause = False
esc = False
playerHP = 0

win = pygame.display.set_mode((500, 500))

class Game:
    def background():
        global win
        win.blit(bg, (0, 0))

    def menu(x, y):
        global playerHP
        global menu
        global Pause
        if menu:
            Pause = False
            while playerHP < 18:
                playerHP += 1
                time.sleep(0.01)
            win.blit(button1, (250, 430 - (45/2)))
            font = pygame.font.Font('munro\munro.ttf', 32)
            text = font.render("START", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (210, 430)
            win.blit(text, textRect)
            keys = pygame.key.get_pressed()
            if y < 430 and y > 385 and x > 250 and x < 295:
                if keys[pygame.K_e]:
                    pygame.mixer.music.load('button_sound.mp3')
                    pygame.mixer.music.play(0)
                    menu = False

    def pause():
        global Pause
        global esc
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            esc = True
            time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and esc == True:
                pygame.mixer.music.load('take-blip.mp3')
                pygame.mixer.music.play(0)
                if Pause == False:
                    Pause = True
                    #time.sleep(0.2)
                else:
                    Pause = False
                    #time.sleep(0.2)
                esc = False
                print(Pause)
        if Pause:
            Game.pause_menu()
        elif menu == False:
            win.blit(escup, (25, 25))

    def pause_menu():
        global Pause
        global menu
        win.blit(escdown, (25, 25))
        font = pygame.font.Font('munro\munro.ttf', 40)
        text = font.render("PAUSED", True, (20, 20, 20))
        textRect = text.get_rect()
        textRect.center = (260, 90)
        win.blit(text, textRect)


    def hp():
        global win
        global playerHP
        hp = playerHP
        if hp == 18:
            win.blit(hp00, (300, 10))
        elif hp == 17:
            win.blit(hp01, (300, 10))
        elif hp == 16:
            win.blit(hp02, (300, 10))
        elif hp == 15:
            win.blit(hp03, (300, 10))
        elif hp == 14:
            win.blit(hp03, (300, 10))
        elif hp == 13:
            win.blit(hp04, (300, 10))
        elif hp == 12:
            win.blit(hp05, (300, 10))
        elif hp == 11:
            win.blit(hp06, (300, 10))
        elif hp == 10:
            win.blit(hp07, (300, 10))
        elif hp == 9:
            win.blit(hp08, (300, 10))
        elif hp == 8:
            win.blit(hp09, (300, 10))
        elif hp == 7:
            win.blit(hp10, (300, 10))
        elif hp == 6:
            win.blit(hp11, (300, 10))
        elif hp == 5:
            win.blit(hp12, (300, 10))
        elif hp == 4:
            win.blit(hp13, (300, 10))
        elif hp == 3:
            win.blit(hp14, (300, 10))
        elif hp == 2:
            win.blit(hp15, (300, 10))
        elif hp == 1:
            win.blit(hp16, (300, 10))
        elif hp == 0:
            win.blit(hp17, (300, 10))
        else:
            win.blit(hp18, (300, 10))



    def main(x, y):
        Game.background()
        Game.menu(x, y)
        Game.pause()
        Game.hp()
