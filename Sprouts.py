from random import randint # импорт необходимых модулей
import tkinter as tk
from tkinter import messagebox
import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Sprouts")


def crossline(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):  # функция на проверку пересечения линий
    v1 = (bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)
    v2 = (bx2 - bx1) * (ay2 - by1) - (by2 - by1) * (ax2 - bx1)
    v3 = (ax2 - ax1) * (by1 - ay1) - (ay2 - ay1) * (bx1 - ax1)
    v4 = (ax2 - ax1) * (by2 - ay1) - (ay2 - ay1) * (bx2 - ax1)
    return v1 * v2 < 0 and v3 * v4 < 0


font = pygame.font.Font("GorgeousPixel.ttf", 36) # задаем шрифт для текста
lose = 0 # инициализируем переменную для отслеживания поражения
close = pygame.image.load('ok.png').convert_alpha() # загружаем изображения

ar_left, ar_right = pygame.image.load('arrow_left.png').convert_alpha(), pygame.image.load(
    'arrow_right.png').convert_alpha()
optionss = pygame.image.load('opionss.png').convert_alpha()
fail = pygame.image.load('error.png').convert_alpha()
image = pygame.image.load('glavnfon.png').convert_alpha()
image1 = pygame.image.load('fon.png').convert_alpha()
sdadit = pygame.image.load('surrer.png').convert_alpha()
image4 = pygame.image.load('start.png').convert_alpha()
image5 = pygame.image.load('winfon.png').convert_alpha()
player1 = pygame.image.load('player1.png').convert_alpha()
player2 = pygame.image.load('player2.png').convert_alpha()
winstr = pygame.image.load('win.png').convert_alpha()
options = pygame.image.load('optionsfon.jpg').convert_alpha()
winf = pygame.image.load('winf.jpg').convert_alpha()
again = pygame.image.load('снова.png').convert_alpha()
fon_list = [image1, image5] # создаем спсиок изображений фонов
fon_list_name = [font.render('Earth', True, (0, 0, 0)), font.render('Field', True, (0, 0, 0))] #  cоздаем список названий фонов
chosenfon = 0 # Изначально выбранный фон
widthline = 1 # Задаем ширину линии
def show_modal_window():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True) # установка флага "always on top"
    messagebox.showinfo("Правила", "Игроки по очереди ходят. Каждый ход игрока состоит в том, что он либо соединяет две точки линией (прямой или кривой), либо рисует линию-петлю, начинающуюся в какой-нибудь точке и в этой же точке заканчивающуюся.\nНа каждой проведённой линии рисуется одна новая точка; новые точки равноправны первоначальным (от них также можно проводить линии, на каждой из которых также рисуется по одной точке).\nПри этом должны соблюдаться следующие правила:\nЛинии не должны пересекаться (самопересечения линий тоже недопустимы).\nПроводимая линия не должна проходить через ранее поставленные точки, не являющиеся началом или концом этой линии, — она может от одной точки начинаться и в другой или в той же точке заканчиваться, а больше никаких касаний линией точек быть не должно.\nИз каждой точки не должно исходить более трёх линий. Поэтому к новой точке нельзя пририсовать петлю, поскольку иначе получится 4 исходящие линии (петля считается двумя исходящими от точки линиями, плюс новая точка уже лежит на линии, то есть от неё уже исходит две линии).\nПроигрывает тот игрок, который не сможет сделать ход, когда в очередной раз наступит его очередь ходить. Можно также играть в поддавки — в этом случае тот, кто сходит последним, считается не выигравшим, а, наоборот, проигравшим.")

    root.destroy()

    # Блокировка основного окна Pygame
    pygame.display.set_mode((800, 600), pygame.NOFRAME)
    pygame.display.set_caption("")
dots, line, chosedot = [], [], [0, 0] # создаем пустые списки для точек и линий, а также переменные для выбранной точки и игрока
pl, dotcheck = 1, 0
dotscolor, linecolor = (0, 133, 0), (57, 230, 57) # задаем цвета точек и линий
linex, liney, newdot, x, y = 0, 0, (0, 0), 0, 0
game, dot_line_dot, dot_append, win, dot = True, False, False, False, False # изначально линия не нарисована, новая точка не добавлена, победы и точка-точка-линия не достигнуты
changefon, changewidth = font.render('Change background', True, (0, 0, 0)), font.render('Change line width', True,
                                                                                        (0, 0, 0)) # задаем текст для кнопок изменения фона и толщины линии
FPS = 60 # задаем FPS и начальные значения для экранов начала и настроек
begin, setting = True, False

while game:  # цикл игры
    clock.tick(FPS)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:  # выход из игры
            game = False
        if ev.type == pygame.MOUSEMOTION:  # движения мыши
            x = ev.pos[0]
            y = ev.pos[1] # получаем координаты мыши
            if dot_append: # если есть пересечение, устанавливаем новую точку на пересечении
                for i in line:
                    if 400 > ((x - i[0]) * (i[3] - i[1]) - (y - i[1]) * (i[2] - i[0])) > -400:
                        if (i[0] + 10 > x > i[2] - 10 and 10 + i[1] > y > i[3] - 10) or (
                                i[0] + 10 < x < i[2] - 10 and 10 + i[1] < y < i[3] - 10) or (
                                i[0] + 10 > x > i[2] - 10 and 10 + i[1] < y < i[3] - 10) or (
                                i[0] + 10 < x < i[2] - 10 and 10 + i[1] > y > i[3] - 10):
                            newdot = (x, y)

        if ev.type == pygame.MOUSEBUTTONDOWN:  # нажатие на кнопку мыши
            if ev.button == 1:
                if win:  # перезапуск
                    win = False
                    begin = True
                    dots.clear()
                    line.clear()
                else:
                    if not begin and 0 <= x <= 95 and 0 <= y <= 65:  # сдаться
                        win = True
                    if not begin and 705 <= x <= 800 and 0 <= y <= 65:  # сдаться
                        show_modal_window()

                        pygame.display.set_mode((800, 800))
                        pygame.display.set_caption("Pygame")
                    if begin and 0 <= x <= 90 and 0 <= y <= 65:  # настройки
                        setting = True
                    if setting:# переход в настройки
                        if 50 <= x <= 200 <= y <= 280:  # фон
                            if chosenfon != 0:
                                chosenfon -= 1
                        if WIDTH - 200 <= x <= WIDTH - 50 and 200 <= y <= 280:
                            if chosenfon != len(fon_list) - 1:
                                chosenfon += 1
                        if 50 <= x <= 200 and 500 <= y <= 580:  # толщина
                            if widthline != 1:
                                widthline -= 1
                        if WIDTH - 200 <= x <= WIDTH - 50 and 500 <= y <= 580:
                            if widthline != 3: 
                                widthline += 1
                        if WIDTH // 2 - 50 <= x <= WIDTH // 2 + 50 and 600 <= y <= 700:  # выход настроек
                            setting = False

                    for i in line:  # если координаты точки пересекаются с линией, используя функцию crossline, и линия пересекается с точкой, устанавливаем новую точку на пересечении
                        if crossline(x, y, linex + 1, liney + 1, i[0], i[1], i[2], i[3]) and crossline(x, y,
                                                                                                         linex - 1,
                                                                                                         liney - 1,
                                                                                                         i[0],
                                                                                                         i[1], i[2],
                                                                                                         i[3]):
                            dot = True

                    for i in dots:  # проверка победы
                        if i[2] == 3:
                            lose += 1
                        if lose == len(dots):
                            win = True
                    lose = 0
                    # кнопка начала игры
                    if (WIDTH // 2 - 150 <= x <= WIDTH // 2 + 150) and (
                            HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 250) and begin and not setting:
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        dots.append([randint(100, WIDTH - 100), randint(100, HEIGHT - 100), 0])
                        begin = False

                    if dot_line_dot:  # линия петля

                        for i in dots:
                            if x <= chosedot[0] <= x + 20 and y <= chosedot[1] <= y + 20:
                                pass
                            else:
                                if i[0] <= x <= i[0] + 20 and i[1] <= y <= i[1] + 20:  # если точка выбрана, проводим линию к ней
                                    if i[2] < 3:
                                        if not dot_append:
                                            i[2] += 1
                                            line.append([x, y, linex, liney, widthline])
                                            dot_append = True
                                            dot_line_dot = False
                                else:
                                    if not dot_append:  # если точка не выбрана, просто проводим линию

                                        chosedot = [0, 0]
                                        line.append([x, y, linex, liney, widthline])
                                        linex = x
                                        liney = y

                    else:
                        for i in dots:  # выбирается точка
                            if i[0] <= x <= i[0] + 20 and i[1] <= y <= i[1] + 20 and i[2] < 3 and not dot_append and not dot:
                                    linex = x
                                    liney = y
                                    chosedot = [x, y]
                                    i[2] += 1
                                    dot_line_dot = True
                        if dot_append and newdot[0] > 0 and newdot[1] > 0:  # смена игрока
                            dots.append([newdot[0], newdot[1], 2])
                            dot_append = False
                            if pl == 1:
                                pl = 2  
                            else:
                                pl = 1

                    if dot:  # отрисовка сообщения
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
            screen.blit(image, (0, 0))  # старт
            screen.blit(image4, (WIDTH // 2 - 150, HEIGHT // 2 + 100))
            pygame.draw.rect(screen, (125, 125, 125), (0, 0, 90, 65), 0)
            screen.blit(optionss, (5, 25))
    elif not win:  # отрисовка игры

        screen.blit(fon_list[chosenfon], (0, 0))
        pygame.draw.rect(screen, (125, 125, 125), (0, 0, 95, 65), 0)
        screen.blit(sdadit, (5, 25))
        pygame.draw.rect(screen, (125, 125, 125), (705, 0, 95, 65), 0)
        screen.blit(font.render("RULES",True,(255,255,255)), (710, 10))
        if dot:
            screen.blit(fail, (WIDTH // 2, HEIGHT // 2))
        if pl == 1:  # очередь хождения
            screen.blit(player1, (WIDTH // 2 - 60, 10))
        else:
            screen.blit(player2, (WIDTH // 2 - 60, 10))
        if newdot[1] > 0 and newdot[0] > 0:  # отрисовка точки на линии
            pygame.draw.circle(screen, (0, 133, 0),newdot,10)
        if dot_line_dot:  # отрисовка линии которую ставят
            pygame.draw.line(screen, linecolor, [linex, liney], [x, y], widthline)
        for i in line:  # отрисовка линий
            if i[0] == i[2] and i[1] == i[3]:
                line.remove(i)
            pygame.draw.line(screen, linecolor, [i[0], i[1]], [i[2], i[3]], i[4])
        for i in dots:  # отрисовка точек
            pygame.draw.circle(screen, (0, 133, 0),(i[0],i[1]),10)

    else:  # отрисовка результата
        screen.blit(winf, (0, 0))
        screen.blit(winstr, (WIDTH // 2 - 60, HEIGHT // 2 - 90))
        screen.blit(again, (WIDTH // 2 - 60, HEIGHT // 2 + 150))
        if pl != 1: # если ходит 1 игрок, то отображетя его иконка
            screen.blit(player1, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        else: # если 2 игрок, то его
            screen.blit(player2, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
    pygame.display.update()
