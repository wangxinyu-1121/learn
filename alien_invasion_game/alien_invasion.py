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
        # 调用设置类
        self.settings = Settings()

        # 设置游戏窗口、背景色和标题
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置全屏
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # 设置游戏背景色和标题
        self.background_color = self.settings.background_color
        pygame.display.set_caption("外星人入侵")

        # 设置飞船
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """响应松键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕上"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.background_color)
        # 绘制飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
