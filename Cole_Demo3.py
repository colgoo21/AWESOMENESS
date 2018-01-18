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

player = Sprite(350, 450)

gameloop = True
while gameloop:
    for event in pygame.event.get():
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