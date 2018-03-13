import pygame
import random

WIDTH = 400
HEIGHT = 300
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG BETA")
clock = pygame.time.Clock()
FONT = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(FONT, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 64))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 50
        self.rect.bottom = HEIGHT/2
        self.speedy = 0
        self.score = 0
        self.scoreFont = pygame.font.Font(FONT, 64)

    def update(self):
        draw_text(screen, str(self.score), 8, (WIDTH / 2) + 8, HEIGHT / 2)
        self.scoring()
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def scoring(self):
        if self.score == 10:
            game_over_screen_p2()


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 64))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = HEIGHT/2
        self.speedy = 0
        self.score = 0
        self.scoreFont = pygame.font.Font(FONT, 64)

    def update(self):
        draw_text(screen, str(self.score), 8, (WIDTH / 2) + 8, HEIGHT / 2)
        self.scoring()
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_s]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def scoring(self):
        if self.score == 10:
            game_over_screen_p1()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2
        self.speedx = 5
        self.speedy = -5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y <= 0:
            self.speedy *= -1
        if self.rect.bottom >= HEIGHT:
            self.speedy *= -1
        if self.rect.x <= 0:
            self.__init__()
            player2.score += 1
        if self.rect.x + 8 >= WIDTH:
            self.__init__()
            self.speedx *= -1
            player1.score += 1
        for x in range(0, 64):
            if self.rect.y == player2.rect.y + x:
                if self.rect.x >= player2.rect.x - 16:
                    self.speedx *= -1
                    break
            if self.rect.y == player1.rect.y + x:
                if self.rect.x <= player1.rect.x + 16:
                    self.speedx *= -1
                    break


def game_over_screen_p1():
    draw_text(screen, "Player 1 wins!!", 32, WIDTH/2, 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYUP:
                waiting = False

def game_over_screen_p2():
    draw_text(screen, "Player 2 wins!!", 32, WIDTH/2, 20)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYUP:
                waiting = False


all_sprites = pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(Ball())

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
