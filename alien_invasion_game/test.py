#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
from settings import Settings

"""初始化游戏并创建游戏资源"""
pygame.init()
# 调用设置类
settings = Settings()

# screen = pygame.display.set_mode((1200, 800))
screen = pygame.display.set_mode([settings.screen_width, settings.screen_height])

pygame.display.set_caption("外星人入侵")

# 设置背景色
# background_color = (230, 230, 230)
background_color = settings.background_color

"""开始游戏的循环"""
# 每次循环时都重绘屏幕
screen.fill(background_color)
# 让最近绘制的屏幕可见
pygame.display.flip()

while True:
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 更新屏幕内容
    pygame.display.update()
