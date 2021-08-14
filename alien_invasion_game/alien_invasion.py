#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
from Settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        #调用设置类
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
        # 标题
        pygame.display.set_caption("外星人入侵")

        # 设置飞船
        self.ship = Ship(self)

        # 设置背景色
        # self.background_color = (230, 230, 230)
        self.background_color = self.settings.background_color

    def run_game(self):
        """开始游戏的循环"""


        while True:

            # 每次循环时都重绘屏幕
            self.screen.fill(self.background_color)
            # 绘制飞船
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # # 更新屏幕内容
            # pygame.display.update()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

