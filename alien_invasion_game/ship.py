import pygame
from Settings import Settings


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

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
