import pygame
import numpy as np
import random

FONT_PX = 20
pygame.init()
winSur = pygame.display.set_mode((800, 1000))                             #构建显示框
font = pygame.font.SysFont('fangsong', 20)                                #字体
bg_suface = pygame.Surface((800, 1000), flags=pygame.SRCALPHA)            #界面设置
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 13))                                 #颜色设置
winSur.fill((0, 0, 0))

texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]

colums = int(800 / FONT_PX)                                               # 按窗口的宽度来计算可以在画板上放几列坐标并生成一个列表
drops = [0 for i in range(colums)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                     #退出窗口设定（关闭窗口按钮检测）
            exit()
    pygame.time.delay(33)
    winSur.blit(bg_suface, (0, 0))
    for i in range(len(drops)):
        text = random.choice(texts)
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))               #surface.blit实现动画
        drops[i] += 1
        if drops[i] * 10 > 600 or random.random() > 0.95:                  #控制数字延申的屏幕长度
            drops[i] = 0
    pygame.display.flip()
