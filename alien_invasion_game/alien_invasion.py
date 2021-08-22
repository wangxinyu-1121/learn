#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from time import sleep

import pygame
from pygame.locals import *
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 调用设置类
        self.settings = Settings()

        # 设置游戏窗口、背景色和标题
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置全屏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # 设置游戏背景色和标题
        self.background_color = self.settings.background_color
        pygame.display.set_caption("外星人入侵")
        # 存储游戏统计信息
        self.stats = GameStats(self)
        # 创建记分牌
        self.sb = Scoreboard(self)

        # 设置飞船
        self.ship = Ship(self)
        # 设置子弹
        self.bullets = pygame.sprite.Group()
        # 设置外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 设置play按钮
        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏的循环"""
        while True:
            self._check_events()

            # 检查需要运行游戏那些部分
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """玩家点击play时开始游戏"""
        button_checked = self.play_button.rect.collidepoint(mouse_pos)
        if button_checked and not self.stats.game_active:
            # 重置游戏速度
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹位置
        self.bullets.update()
        # 消失的子弹，要移除，不然会继续消耗内存和处理能力
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞"""
        # 检查子弹是否击中外星人，是则删除相应子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # 生成新的外星人群
        if collisions:
            # 记分,并记录最高分
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.aliens:
            # 删除现有所有子弹并新建外星人
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳多少个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 计算屏幕容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - ship_height - (3 * alien_height))
        number_rows = available_space_y // (3 * alien_height)
        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """更新外星人群中的所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞创之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达屏幕底部
        self._check_aliens_bottom()

    def _ship_hit(self):
        """响应飞船被外星人碰撞"""
        if self.stats.ships_lift > 0:
            # 将ships_left - 1 并更新记命牌
            self.stats.ships_lift -= 1
            self.sb.prep_ships()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停1秒
            sleep(1)
        else:
            self.stats.game_active = False
            # 游戏结束后光标可见
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """检查是否有飞船到达屏幕底部"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕上"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.background_color)
        # 绘制飞船
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 绘制外星人
        self.aliens.draw(self.screen)
        # 显示得分
        self.sb.show_score()
        # 如果游戏处于非活动状态，绘制play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
