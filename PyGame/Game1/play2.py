import pygame
import random

score=0
screen=pygame.display.set_mode((1000,500))
class MyCar(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((40,50))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 460
        self.rect.y = 400
        self.moveX = 0

    def update(self):
        self.rect.x+=self.moveX
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 6
        elif keypressed[pygame.K_LEFT]:
            self.moveX = -6
        else:
            self.moveX = 0

class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(300,600)
        self.rect.y = random.randint(-1000,0)
        self.moveY = 3

    def update(self):
        self.rect.y+=self.moveY
        if self.rect.top>500:
            self.rect.x = random.randint(300, 600)
            self.rect.y = random.randint(-50, 0)

FPS=100
clock=pygame.time.Clock()


mycar=MyCar()
allCars=pygame.sprite.Group()
enemyCars=pygame.sprite.Group()

allCars.add(mycar)
for i in range(5):
    enemy=EnemyCar()
    allCars.add(enemy)
    enemyCars.add(enemy)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    hit=pygame.sprite.spritecollide(mycar,enemyCars,True)
    if hit:
        pygame.quit()
        quit()
    screen.fill((255,255,255))

    pygame.draw.rect(screen,(0,0,0),[0,0,300,500])
    pygame.draw.rect(screen, (0, 0, 0), [700, 0, 300, 500])
    allCars.draw(screen)
    allCars.update()
    pygame.display.update()

    clock.tick(FPS)
