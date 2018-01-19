import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SPACE INVADERS BETA")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

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

    def shoot(self):
        laser = Laser(self.)


player = Sprite(350, 450)


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def render(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


gameloop = True
while gameloop:
    for event in pygame.event.get():
        if player.x <= 0:
            player.x = 0

        if player.x >= 550:
            player.x = 550

        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                moveX = -5

            if event.key == pygame.K_RIGHT:
                moveX = 5

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                moveX = 0

            if event.key == pygame.K_RIGHT:
                moveX = 0

    window.fill(black)
    player.x += moveX
    player.render()
    clock.tick(50)
    pygame.display.flip()
pygame.quit()
