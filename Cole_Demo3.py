import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SPACE INVADERS BETA")

black = (0, 0, 0)
white = (255, 255, 255)


moveX = 0

clock = pygame.time.Clock()

class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = pygame.image.load('alien.png')

    def render(self):
        window.blit(self.image, (self.x, self.y))

    def shoot_bullet(self):
        bullet = pygame.image.load('bullet.png')
        self.width = 5
        self.height = 30
        bullet.x = player.x
        bullet.y = 0
        while bullet.y != 550:
            bullet += 1
        if bullet.y == 570:
            del(bullet)

    def dont_shoot_bullet(self):
        del(self.shoot_bullet)

class Enemy:
    def __init__(self, x, y):
        # 8 by 5
        self.x = x
        self.y = y
        self.width = 50
        self.height = 17
        enemy = pygame.image.load('enemy.png')

    def eight_by_five(self):
        enemy = 0
        while enemy != 40:
            enemy.x = 0
            enemy.y = 0
            enemy.x += 10
            enemy += 1
            if enemy % 8 == 0:
                enemy.x = 0
                enemy.y = 20

class Shield:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 15
        shield = pygame.image.load('shield.png')

    def four_shields(self):
        shield = 0
        shield.x = 175
        shield.y = 100
        while shield != 4:
            shield.x += 175
            shield += 1


player = Sprite(350, 450)

gameloop = True
while gameloop:
    for event in pygame.event.get():
        if player.x <= 0:
            player.x = 0
        if player.x >= 750:
            player.x = 750
        if event.type == pygame.QUIT:
            gameloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -5
            if event.key == pygame.K_RIGHT:
                moveX = 5
            if event.key == pygame.K_SPACE:
                player.shoot_bullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveX = 0
            if event.key == pygame.K_RIGHT:
                moveX = 0
            if event.key == pygame.K_SPACE:
                player.dont_shoot_bullet()

    window.fill(black)
    player.x += moveX
    player.render()
    clock.tick(50)
    pygame.display.flip()
pygame.quit()
