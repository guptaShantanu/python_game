import pygame
import random


score=0
crashed=0
width = 1000
height = 500
white=255,255,255
red=255,0,0
a=100
screen = pygame.display.set_mode((width,height))
# image=pygame.image.load('space.jpg')
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('plane.png').convert()
        # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = width/2 - 25
        self.rect.y = height - 100
        self.moveX = 0



    def update(self):
        self.rect.x += self.moveX

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 6
        elif keypressed[pygame.K_LEFT]:
            self.moveX = -6
        else:
            self.moveX = 0

    def triggerBullet(self,count):
        if count==2:
            bullet_1=Bullet(self.rect.x+15,self.rect.top)
            bullet_2 = Bullet(self.rect.x+25, self.rect.top)
            all_sprites.add(bullet_1)
            all_sprites.add(bullet_2)
            bulletGroup.add(bullet_1)
            bulletGroup.add(bullet_2)
        elif count==1:
            bullet_1 = Bullet(self.rect.x + 30, self.rect.top)
            all_sprites.add(bullet_1)
            bulletGroup.add(bullet_1)

        elif count==3:
            bullet_1 = Bullet(self.rect.x + 10, self.rect.top)
            bullet_2 = Bullet(self.rect.x + 20, self.rect.top-10)
            bullet_3 = Bullet(self.rect.x + 30, self.rect.top)
            all_sprites.add(bullet_1)
            all_sprites.add(bullet_2)
            all_sprites.add(bullet_3)
            bulletGroup.add(bullet_1)
            bulletGroup.add(bullet_2)
            bulletGroup.add(bullet_3)



class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load('bullet.png').convert()
        self.image = pygame.Surface((5,10))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.moveY = -10

    def update(self):
        self.rect.y+=self.moveY

        if self.rect.top<0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load('download.png').convert()
        self.image = pygame.Surface((random.randint(55,65),random.randint(55,65)))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 50)
        self.rect.y = random.randint(-height*20, 0)
        self.moveY = random.randint(2,5)
#
    def update(self):
        self.rect.y+=self.moveY

        if self.rect.top>height:
            self.rect.x = random.randint(0, width - 50)
            self.rect.y = random.randint(-height*10, 0)

def Health(blood):
    dist=10
    for i in range(blood):

        pygame.draw.rect(screen,red,[dist,10,20,20])
        dist+=40

player=Player()
all_sprites = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
all_sprites.add(player)

# pygame.draw.circle(screen,(0,0,0),(20,20),20)

for i in range(50):
    enemy=Enemy()
    enemyGroup.add(enemy)
    all_sprites.add(enemy)

blood=5
FPS=100
clock=pygame.time.Clock()
while True:
    if score<20:
        num=1
    elif score<40 and score>20:
        num=2
    elif score>40:
        num=3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.triggerBullet(num)

    hit=pygame.sprite.groupcollide(bulletGroup,enemyGroup,True,True)

    if hit:
        crashed+=1
        score+=1

        if crashed==50:
            print("you won the game")
            pygame.quit()
            quit()

    crash=pygame.sprite.spritecollide(player,enemyGroup,True)
    if crash:
        crashed+=1
        blood=blood-1

        if blood==0:
            print("YOU LOSE")
            pygame.quit()
            quit()

        if crashed==50:
            print("YOU WON")
            pygame.quit()
            quit()

    #
    # screen.blit(image, (0,0))
    screen.fill(white)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.draw.circle(screen, (0, 0, 0), (20, 20), 20)
    Health(blood)
    pygame.display.update()

    clock.tick(FPS)
    print(score,crashed)
