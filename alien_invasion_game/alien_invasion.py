import sys
import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("外星人入侵")

    def run_game(self):
        """开始游戏的循环"""
        while True:
            # 监视键盘和鼠标事件
            for user_event in pygame.event.get():
                if user_event.type == pygame.QUIT:
                    sys.q=exit()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__name__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
