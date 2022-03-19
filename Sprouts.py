from email.mime import image
from tkinter import W
from turtle import width
import pygame
from random import randint


def crossline(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):# функция на проверку пересечения линий
    v1 = (bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)
    v2 = (bx2 - bx1) * (ay2 - by1) - (by2 - by1) * (ax2 - bx1)
    v3 = (ax2 - ax1) * (by1 - ay1) - (ay2 - ay1) * (bx1 - ax1)
    v4 = (ax2 - ax1) * (by2 - ay1) - (ay2 - ay1) * (bx2 - ax1)
    return v1 * v2 < 0 and v3 * v4 < 0


pygame.init()
pygame.mixer.init()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

lose = 0
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
close = pygame.image.load('close.png').convert_alpha()
ar_left,ar_right =pygame.image.load('arrow_left.png').convert_alpha(),pygame.image.load('arrow_right.png').convert_alpha()
image = pygame.image.load('logo.jpg').convert_alpha()
image1 = pygame.image.load('fon.png').convert_alpha()
image2 = pygame.image.load('seed.png').convert_alpha()
#image3 = pygame.image.load('surrer.png').convert_alpha()
image4 = pygame.image.load('start.png').convert_alpha()
image5 = pygame.image.load('winfon.png').convert_alpha()
fon_list = [image1, image5]
fon_list_name = [font.render('Земля', True, (0, 0, 0)),font.render('Поле', True, (0, 0, 0))]
chosenfon = 0
widthline = 1

dots, line = [], []
pl = 1
dotscolor, linecolor = (0, 133, 0), (57, 230, 57)
linex, liney, newdot = 0, 0, (0, 0)
game, dot_line_dot, dot_append, win, dot = True, False, False, False, False
fontm = pygame.font.Font(pygame.font.get_default_font(), 12)
winstr = font.render('Победил', True, (0, 0, 0))
player1, player2 = font.render('Игрок 1', True, (0, 0, 0)), font.render('Игрок 2', True, (0, 0, 0))
sdas = fontm.render('Сдаться', True, (0, 0, 0))
settingtext = fontm.render('Настройки', True, (0, 0, 0))
changefon, changewidth = font.render('Сменить фон', True, (0, 0, 0)),font.render('Поменять ширину линии', True, (0, 0, 0))
FPS = 60
WIDTH = 800
HEIGHT = 800
begin, setting = True , False
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
color = (125, 0, 0)

pygame.display.set_caption("Sprouts")

while game: # цикл игры
    clock.tick(FPS)
    screen.fill(WHITE)
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                if widthline > 0:
                    widthline -=1
            if ev.key == pygame.K_RIGHT:
                widthline +=1
        if ev.type == pygame.QUIT:# выход из игры
            game = False
        if ev.type == pygame.MOUSEMOTION:# движения мыши
            x = ev.pos[0]
            y = ev.pos[1]
            if (WIDTH // 2 - 60 <= x <= WIDTH // 2 + 90) and (HEIGHT // 2 + 175 <= y <= HEIGHT // 2 + 275) and begin:
                color = (125, 125, 125)
            else:
                color = (125, 0, 0)
            if dot_append:
                for i in line:
                    if 400 > ((x - i[0]) * (i[3] - i[1]) - (y - i[1]) * (i[2] - i[0])) > -400:
                        if (i[0] + 10 > x > i[2] - 10 and 10 + i[1] > y > i[3] - 10) or (
                                i[0] + 10 < x < i[2] - 10 and 10 + i[1] < y < i[3] - 10) or (
                                i[0] + 10 > x > i[2] - 10 and 10 + i[1] < y < i[3] - 10) or (
                                i[0] + 10 < x < i[2] - 10 and 10 + i[1] > y > i[3] - 10):
                            newdot = (x, y)

        if ev.type == pygame.MOUSEBUTTONDOWN:# нажатие на кнопку мыши
            if ev.button == 1:
                print(x," ",y)
                if not begin and 0 <= x <= 65 and 0 <= y <= 65:
                    win = True

                if begin and 0 <= x <= 65 and 0 <= y <= 65:
                    setting = True
                if setting:
                    if 50 <= x <= 200 and 200 <= y <= 280:
                        if chosenfon!=0:
                            chosenfon-=1
                    if WIDTH-200 <= x <= WIDTH-50 and 200 <= y <= 280:
                        if chosenfon!=len(fon_list)-1:
                            chosenfon+=1
                    if 50 <= x <= 200 and 500 <= y <= 580:
                        if widthline!=1:
                            widthline-=1
                    if WIDTH-200 <= x <= WIDTH-50 and 500 <= y <= 580:
                        if widthline!=3:
                            widthline+=1
                    if WIDTH // 2 - 50 <= x <= WIDTH // 2 + 50 and 600 <= y <= 700:
                        setting = False
                for i in line:
                    if crossline(x, y, linex, liney, i[0], i[1], i[2], i[3]):
                        dot = True
                        for j in dots:
                            if j[0] - 10 <= linex <= j[0] + 10 and j[1] - 10 <= liney <= j[1] + 10:
                                dot = False

                for i in dots:
                    if i[2] == 3:
                        lose += 1
                    if lose == len(dots):
                        win = True
                lose = 0

                if (WIDTH // 2-150 <= x <=WIDTH // 2+150) and (HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 250) and begin and not setting:
                    dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                    dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                    dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                    dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                    dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                    dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                    begin = False

                if dot_line_dot:
                    for i in dots:

                        if i[0] - 10 <= x <= i[0] + 10 and i[1] - 10 <= y <= i[1] + 10:
                            if i[2] < 3:
                                if not dot:
                                    i[2] += 1
                                    line.append([x, y, linex, liney,widthline])
                                    dot_append = True
                                    dot_line_dot = False

                        else:
                            if not dot:
                                line.append([x, y, linex, liney,widthline])
                                linex = x
                                liney = y
                else:
                    for i in dots:
                        if i[0] - 20 <= x <= i[0] + 20 and i[1] - 20 <= y <= i[1] + 20 and i[2] < 3 and not dot_line_dot:
                            linex = x
                            liney = y
                            i[2] += 1
                            dot_line_dot = True
                    if dot_append and newdot[0] > 0 and newdot[1] > 0:
                        dots.append([newdot[0], newdot[1], 2])
                        dot_append = False
                        if pl == 1:
                            pl = 2
                        else:
                            pl = 1

                dot = False

    if begin: # отрисовка начального экрана
        if setting: 
            screen.blit(changefon, (WIDTH // 2-120, 100))
            screen.blit(ar_left, (50, 200))
            screen.blit(fon_list_name[chosenfon], (WIDTH // 2-50, 200))
            screen.blit(ar_right, (WIDTH-200, 200))
            screen.blit(changewidth, (WIDTH // 2-200, 400))
            screen.blit(ar_left, (50, 500))
            widthline_name = font.render(str(widthline), True, (0, 0, 0))
            screen.blit(widthline_name, (WIDTH // 2, 540))
            screen.blit(ar_right, (WIDTH-200, 500))
            screen.blit(close, (WIDTH // 2 - 50, 600))
            

        else:
            screen.blit(image, (0, 0))
            screen.blit(image4, (WIDTH // 2-150, HEIGHT // 2 + 100))
            pygame.draw.rect(screen, (125, 125, 125), (0, 0, 65, 65), 0)
            screen.blit(settingtext, (5, 25))
        

        
    elif not win: # отрисовка игры
        screen.blit(fon_list[chosenfon], (0, 0))
        pygame.draw.rect(screen, (125, 125, 125), (0, 0, 65, 65), 0)
        screen.blit(sdas, (5, 25))
        if pl == 1:
            screen.blit(player1, (WIDTH // 2 - 60, 10))
        else:
            screen.blit(player2, (WIDTH // 2 - 60, 10))
        if newdot[1] > 0 and newdot[0] > 0:
            screen.blit(image2, newdot,)
        if dot_line_dot:
            pygame.draw.line(screen, linecolor, [linex, liney], [x, y],widthline)
        for i in line:
            if i[0] == i[2] and i[1] == i[3]:
                line.remove(i)
            pygame.draw.line(screen, linecolor, [i[0], i[1]], [i[2], i[3]],i[4])
        for i in dots:
            screen.blit(image2, (i[0], i[1]),)
    else: # отрисовка результата
        screen.blit(winstr, (WIDTH // 2 - 60, HEIGHT // 2 - 70))
        if pl != 1:
            screen.blit(player1, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        else:
            screen.blit(player2, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
    pygame.display.update()
