import pygame

FPS = 60
WIDTH = 500
HEIGHT = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("我的游戏")

running = True
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#  游戏循环
while running:
    clock.tick(FPS)
    # 　取得输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏
    all_sprites.update()

    # 画面显示
    screen.fill(WHITE)

    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()
