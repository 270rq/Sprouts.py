from random import randint

import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.font.init()


def crossline(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):  # функция на проверку пересечения линий
    v1 = (bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)
    v2 = (bx2 - bx1) * (ay2 - by1) - (by2 - by1) * (ax2 - bx1)
    v3 = (ax2 - ax1) * (by1 - ay1) - (ay2 - ay1) * (bx1 - ax1)
    v4 = (ax2 - ax1) * (by2 - ay1) - (ay2 - ay1) * (bx2 - ax1)
    return v1 * v2 < 0 and v3 * v4 < 0


font = pygame.font.Font("C:/Users/acer/AppData/Local/Microsoft/Windows/Fonts/GorgeousPixel.ttf", 36)
lose = 0
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
close = pygame.image.load('ok.png').convert_alpha()

ar_left, ar_right = pygame.image.load('arrow_left.png').convert_alpha(), pygame.image.load(
    'arrow_right.png').convert_alpha()
music = pygame.mixer.Sound("fonm.wav")
music.play(1)
optionss = pygame.image.load('opionss.png').convert_alpha()
fail = pygame.image.load('error.png').convert_alpha()
image = pygame.image.load('glavnfon.png').convert_alpha()
image1 = pygame.image.load('fon.png').convert_alpha()
image2 = pygame.image.load('seed.png').convert_alpha()
sdadit = pygame.image.load('surrer.png').convert_alpha()
image4 = pygame.image.load('start.png').convert_alpha()
image5 = pygame.image.load('winfon.png').convert_alpha()
player1 = pygame.image.load('player1.png').convert_alpha()
player2 = pygame.image.load('player2.png').convert_alpha()
winstr = pygame.image.load('win.png').convert_alpha()
options = pygame.image.load('optionsfon.jpg').convert_alpha()
winf = pygame.image.load('winf.jpg').convert_alpha()
again = pygame.image.load('снова.png').convert_alpha()
fon_list = [image1, image5]
fon_list_name = [font.render('Earth', True, (0, 0, 0)), font.render('Field', True, (0, 0, 0))]
chosenfon = 0
widthline = 1

dots, line, chosedot = [], [], [0, 0]
pl, dotcheck = 1, 0
dotscolor, linecolor = (0, 133, 0), (57, 230, 57)
linex, liney, newdot = 0, 0, (0, 0)
game, dot_line_dot, dot_append, win, dot = True, False, False, False, False
changefon, changewidth = font.render('Change background', True, (0, 0, 0)), font.render('Change line width', True,
                                                                                        (0, 0, 0))
FPS = 60
WIDTH = 800
HEIGHT = 800
begin, setting = True, False
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
color = (125, 0, 0)

pygame.display.set_caption("Sprouts")

while game:  # цикл игры
    clock.tick(FPS)
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                if widthline > 0:
                    widthline -= 1
            if ev.key == pygame.K_RIGHT:
                widthline += 1
        if ev.type == pygame.QUIT:  # выход из игры
            game = False
        if ev.type == pygame.MOUSEMOTION:  # движения мыши
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

        if ev.type == pygame.MOUSEBUTTONDOWN:  # нажатие на кнопку мыши
            if ev.button == 1:
                if win:
                    win = False
                    begin = True
                    dots.clear()
                    line.clear()
                else:
                    if not begin and 0 <= x <= 95 and 0 <= y <= 65:
                        win = True

                    if begin and 0 <= x <= 90 and 0 <= y <= 65:
                        setting = True
                    if setting:
                        if 50 <= x <= 200 <= y <= 280:
                            if chosenfon != 0:
                                chosenfon -= 1
                        if WIDTH - 200 <= x <= WIDTH - 50 and 200 <= y <= 280:
                            if chosenfon != len(fon_list) - 1:
                                chosenfon += 1
                        if 50 <= x <= 200 and 500 <= y <= 580:
                            if widthline != 1:
                                widthline -= 1
                        if WIDTH - 200 <= x <= WIDTH - 50 and 500 <= y <= 580:
                            if widthline != 3:
                                widthline += 1
                        if WIDTH // 2 - 50 <= x <= WIDTH // 2 + 50 and 600 <= y <= 700:
                            setting = False

                    for i in line:
                        if crossline(x, y, linex + 20, liney + 20, i[0], i[1], i[2], i[3]) and crossline(x, y, linex - 20,
                                                                                                         liney - 20, i[0],
                                                                                                         i[1], i[2], i[3]):
                            dot = True

                    for i in dots:
                        if i[2] == 3:
                            lose += 1
                        if lose == len(dots):
                            win = True
                    lose = 0

                    if (WIDTH // 2 - 150 <= x <= WIDTH // 2 + 150) and (
                            HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 250) and begin and not setting:
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        begin = False

                    if dot_line_dot:

                        for i in dots:
                            if x - 10 <= chosedot[0] <= x + 10 and y - 10 <= chosedot[1] <= y + 10:
                                pass
                            else:
                                if i[0] - 10 <= x <= i[0] + 10 and i[1] - 10 <= y <= i[1] + 10:
                                    if i[2] < 3:
                                        if not dot:
                                            i[2] += 1
                                            line.append([x, y, linex, liney, widthline])
                                            dot_append = True
                                            dot_line_dot = False
                                else:
                                    if not dot:
                                        chosedot = [0, 0]
                                        line.append([x, y, linex, liney, widthline])
                                        linex = x
                                        liney = y

                    else:
                        for i in dots:
                            if i[0] - 20 <= x <= i[0] + 20 and i[1] - 20 <= y <= i[1] + 20 and i[
                                2] < 3 and not dot_line_dot:
                                linex = x
                                liney = y
                                chosedot = [x, y]
                                i[2] += 1
                                dot_line_dot = True
                        if dot_append and newdot[0] > 0 and newdot[1] > 0:
                            dots.append([newdot[0], newdot[1], 2])
                            dot_append = False
                            if pl == 1:
                                pl = 2
                            else:
                                pl = 1

                    if dot:
                        dotcheck += 1
                    if dotcheck == 2:
                        dot = False
                        dotcheck = 0
    if begin:  # отрисовка начального экрана
        if setting:
            screen.blit(options, (0, 0))
            screen.blit(changefon, (WIDTH // 2 - 180, 100))
            screen.blit(ar_left, (50, 200))
            screen.blit(fon_list_name[chosenfon], (WIDTH // 2 - 50, 200))
            screen.blit(ar_right, (WIDTH - 200, 200))
            screen.blit(changewidth, (WIDTH // 2 - 175, 400))
            screen.blit(ar_left, (50, 500))
            widthline_name = font.render(str(widthline), True, (0, 0, 0))
            screen.blit(widthline_name, (WIDTH // 2, 540))
            screen.blit(ar_right, (WIDTH - 200, 500))
            screen.blit(close, (WIDTH // 2 - 50, 600))
        else:
            screen.blit(image, (0, 0))
            screen.blit(image4, (WIDTH // 2 - 150, HEIGHT // 2 + 100))
            pygame.draw.rect(screen, (125, 125, 125), (0, 0, 90, 65), 0)
            screen.blit(optionss, (5, 25))
    elif not win:  # отрисовка игры

        screen.blit(fon_list[chosenfon], (0, 0))
        pygame.draw.rect(screen, (125, 125, 125), (0, 0, 95, 65), 0)
        screen.blit(sdadit, (5, 25))
        if dot:
            screen.blit(fail, (WIDTH // 2, HEIGHT // 2))
        if pl == 1:
            screen.blit(player1, (WIDTH // 2 - 60, 10))
        else:
            screen.blit(player2, (WIDTH // 2 - 60, 10))
        if newdot[1] > 0 and newdot[0] > 0:
            screen.blit(image2, newdot, )
        if dot_line_dot:
            pygame.draw.line(screen, linecolor, [linex, liney], [x, y], widthline)
        for i in line:
            if i[0] == i[2] and i[1] == i[3]:
                line.remove(i)
            pygame.draw.line(screen, linecolor, [i[0], i[1]], [i[2], i[3]], i[4])
        for i in dots:
            screen.blit(image2, (i[0], i[1]), )
    else:  # отрисовка результата
        screen.blit(winf, (0, 0))
        screen.blit(winstr, (WIDTH // 2 - 60, HEIGHT // 2 - 90))
        screen.blit(again,(WIDTH//2 - 60, HEIGHT//2 + 150))
        if pl != 1:
            screen.blit(player1, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        else:
            screen.blit(player2, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
    pygame.display.update()
