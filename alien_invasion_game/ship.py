import pygame
from settings import Settings


class Ship:
    """管理飞船类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = Settings()
        # 获取屏幕外接矩形
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        # 修改飞船尺寸
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.ship_width, self.settings.ship_height))
        # 获取飞船外接矩形
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部中央位置
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        # 设置移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据self.x更新rect值
        self.rect.x = self.x


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

