import pygame
import random

width = 1200
height = 600
screen = pygame.display.set_mode((width,height))


black = 0,0,0
white = 255,255,255
red = 255,0,0
color_1 = 100,105,150


class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name



    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey((0,128,128))

        return image


class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load('bullet.png').convert()
        self.image = pygame.Surface((10,3))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y+15
        self.moveY = -10

    def update(self):
        self.rect.x+=self.moveY

        if self.rect.top<0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    standingFrames2=[]
    laserFrames=[]
    movingFrames=[]
    fallFrames2=[]
    punchFrames2=[]
    hurtFrames2=[]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet(superman)


        # standing frames
        self.image = spritesheet.getImage(1097, 68, 79, 97)
        self.standingFrames2.append(self.image)
        self.image = spritesheet.getImage(1009, 70, 80, 95)
        self.standingFrames2.append(self.image)
        self.image = spritesheet.getImage(919, 72, 82, 93)
        self.standingFrames2.append(self.image)
        self.image = spritesheet.getImage(831, 70, 80, 95)
        self.standingFrames2.append(self.image)


        #laser farmes
        self.image = spritesheet.getImage(1176, 548, 79, 97)
        self.laserFrames.append(self.image)
        self.image = spritesheet.getImage(1074, 551, 93, 94)
        self.laserFrames.append(self.image)

        #moving frames
        self.image = spritesheet.getImage(731, 73, 90, 92)
        self.movingFrames.append(self.image)
        self.image = spritesheet.getImage(642, 71, 80, 94)
        self.movingFrames.append(self.image)
        self.image = spritesheet.getImage(456, 80, 98, 85)
        self.movingFrames.append(self.image)

        # hurt frames
        self.image = spritesheet.getImage(731, 73, 90, 92)
        self.movingFrames.append(self.image)
        self.image = spritesheet.getImage(642, 71, 80, 94)
        self.movingFrames.append(self.image)
        self.image = spritesheet.getImage(456, 80, 98, 85)
        self.movingFrames.append(self.image)

        # punch frames
        self.image = spritesheet.getImage(366,786,77,99)
        self.hurtFrames2.append(self.image)
        self.image = spritesheet.getImage(457, 784, 77, 101)
        self.hurtFrames2.append(self.image)
        self.image = spritesheet.getImage(544, 785, 79, 100)
        self.hurtFrames2.append(self.image)


        #fall frame
        self.image = spritesheet.getImage(1167, 785, 90, 100)
        self.fallFrames2.append(self.image)
        self.image = spritesheet.getImage(1044, 805, 114, 80)
        self.fallFrames2.append(self.image)
        self.image = spritesheet.getImage(910, 834, 123, 51)
        self.fallFrames2.append(self.image)


        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 400
        self.pos = 0

        self.stand = True
        self.move_right = False
        self.move_left = False
        self.punch = False
        self.superpunch = False
        self.flyingKick = False
        self.fall = False
        self.laser=False
        self.hurt=False


    def laser_fire(self):
        laser=Laser(self.rect.x,self.rect.y)
        all_sprites.add(laser)
        laserGroup.add(laser)



    def update(self):
        self.pos+=2

        keypressed = pygame.key.get_pressed()

        if keypressed[pygame.K_m]:
            self.laser=True
            self.stand=False
            self.fall = False

        elif keypressed[pygame.K_d]:
            self.move_right=True
            self.stand=False
            self.fall = False
        elif keypressed[pygame.K_a]:
            self.move_left=True
            self.stand=False
            self.fall = False
        elif keypressed[pygame.K_l]:
            self.move_left=False
            self.stand=False
            self.fall = False
            self.punch=True
        elif keypressed[pygame.K_w]:
            self.fall = True
        else:
            if self.fall:
                self.stand=False
            else:
                self.stand = True
                self.laser = False
                self.move_left = False
                self.move_right = False
                self.punch=False




        if self.stand:
            frame = self.pos // 30 % len(self.standingFrames2)
            self.image = self.standingFrames2[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))
        elif self.laser:
            frame = self.pos // 30 % len(self.laserFrames)
            self.image = self.laserFrames[frame]
            if frame==1:
                self.laser_fire()
            self.image = pygame.transform.scale(self.image, (150, 150))
        elif self.move_right:
            self.rect.x+=3
            frame = self.pos // 30 % len(self.movingFrames)
            self.image = self.movingFrames[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))

        elif self.punch:
            frame = self.pos // 30 % len(self.punchFrames2)
            self.image = self.punchFrames2[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))

        elif self.move_left:
            self.rect.x-=3
            frame = self.pos // 30 % len(self.movingFrames)
            self.image = self.movingFrames[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))
        elif self.fall:
            frame = self.pos // 30 % len(self.fallFrames2)
            if frame == len(self.fallFrames2) - 1:
                self.rect.y = 430
                self.image = self.fallFrames2[2]
                self.image = pygame.transform.scale(self.image, (150, 150))
                self.pos -= 2

            else:
                self.rect.x += 15
                self.image = self.fallFrames2[frame]
                self.image = pygame.transform.scale(self.image, (150, 150))


class Player(pygame.sprite.Sprite):
    standingFrames=[]
    movingLeftFrames=[]
    movingRightFrames = []
    superpunchFrames = []
    punchFrames=[]
    flyingKickFrames=[]
    fallFrames=[]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet=Spritesheet(batman)

        #standing frames
        self.image=spritesheet.getImage(101,14,97,105)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(206, 16, 100, 103)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(314, 18, 103, 101)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(424, 16, 101, 103)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(532, 14, 78, 105)
        self.standingFrames.append(self.image)


        # moving right frames
        self.image = spritesheet.getImage(424, 16, 101, 103)
        self.movingRightFrames.append(self.image)
        self.image = spritesheet.getImage(532, 14, 78, 105)
        self.movingRightFrames.append(self.image)
        self.image = spritesheet.getImage(4, 9, 90, 110)
        self.movingRightFrames.append(self.image)





        #superpunch frames
        self.image = spritesheet.getImage(677, 181, 109, 100)
        self.superpunchFrames.append(self.image)
        self.image = spritesheet.getImage(795, 179, 101, 102)
        self.superpunchFrames.append(self.image)
        self.image = spritesheet.getImage(904, 186, 164, 95)
        self.superpunchFrames.append(self.image)
        self.image = spritesheet.getImage(1079, 184, 141, 97)
        self.superpunchFrames.append(self.image)



        #punch_frames
        self.image = spritesheet.getImage(406, 177, 103, 104)
        self.punchFrames.append(self.image)
        self.image = spritesheet.getImage(520, 177, 148, 104)
        self.punchFrames.append(self.image)
        self.image = spritesheet.getImage(532, 14, 78, 105)
        self.punchFrames.append(self.image)


        #flying kick
        self.image = spritesheet.getImage(5, 533, 154, 102)
        self.flyingKickFrames.append(self.image)
        self.image = spritesheet.getImage(168, 518, 153, 117)
        self.flyingKickFrames.append(self.image)
        self.image = spritesheet.getImage(313, 543, 99, 92)
        self.flyingKickFrames.append(self.image)
        self.image = spritesheet.getImage(423, 546, 177, 89)
        self.flyingKickFrames.append(self.image)

        #fall frames
        self.image = spritesheet.getImage(6, 934, 100, 106)
        self.fallFrames.append(self.image)
        self.image = spritesheet.getImage(115, 994, 124, 91)
        self.fallFrames.append(self.image)
        self.image = spritesheet.getImage(253, 982, 116, 58)
        self.fallFrames.append(self.image)
















        self.rect=self.image.get_rect()
        self.rect.x=50
        self.rect.y=400
        self.pos = 0

        self.stand = True
        self.move_right = False
        self.move_left=False
        self.punch=False
        self.superpunch=False
        self.flyingKick=False
        self.fall=False


    def update(self):
        self.pos += 2

        keypressed = pygame.key.get_pressed()
        if True:
            if keypressed[pygame.K_RIGHT]:
                self.move_right = True
                self.move_left=False
                self.stand = False
                self.fall=False

            elif keypressed[pygame.K_LEFT]:
                self.move_left = True
                self.move_right=False
                self.stand = False
                self.fall = False
            elif keypressed[pygame.K_k]:
                self.move_left = False
                self.stand = False
                self.fall=True
                self.fall = True

            elif keypressed[pygame.K_z]:
                self.stand=False
                self.move_left=False
                self.move_right=False
                self.punch=True
                self.fall = False

            elif keypressed[pygame.K_SPACE]:
                self.flyingKick=True
                self.stand = False
                self.move_left = False
                self.move_right = False
                self.punch = False
                self.fall=False

            elif keypressed[pygame.K_x]:
                self.superpunch=True
                self.move_right = False
                self.stand = False
                self.move_left = False
                self.punch = False
            elif keypressed[pygame.K_UP]:
                self.fall=False
            else:
                self.stand=True
                self.move_right=False
                self.move_left=False
                self.punch=False
                self.flyingKick=False
                self.superpunch=False



        if self.move_right:
            self.rect.x = self.rect.x + 1
            frame = self.pos // 30 % len(self.movingRightFrames)
            self.image = self.movingRightFrames[frame]
            self.image=pygame.transform.scale(self.image,(150,150))
        elif self.move_left:
            self.rect.x = self.rect.x - 1
            frame = self.pos // 30 % len(self.movingRightFrames)
            self.image = self.movingRightFrames[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))

        elif self.fall:
            frame = self.pos // 30 % len(self.fallFrames)
            if frame==len(self.fallFrames)-1:
                self.rect.y=430
                self.image = self.fallFrames[2]
                self.image = pygame.transform.scale(self.image, (150, 150))
                self.pos-=2

            else:
                self.rect.x-=15
                self.image = self.fallFrames[frame]
                self.image = pygame.transform.scale(self.image, (150, 150))





        elif self.flyingKick:
            frame = self.pos // 30 % len(self.flyingKickFrames)
            self.image = self.flyingKickFrames[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))
            if frame==0 or frame==1:
                self.rect.x+=1
                self.rect.y=350
            else:
                self.rect.x += 1
                self.rect.y =400



        elif self.stand:
            self.rect.y=400
            frame = self.pos // 30 % len(self.standingFrames)
            self.image = self.standingFrames[frame]
            self.image=pygame.transform.scale(self.image,(150,150))

        elif self.superpunch:
            frame = self.pos // 30 % len(self.superpunchFrames)
            self.image = self.superpunchFrames[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))



        elif self.punch:
            frame = self.pos // 30 % len(self.punchFrames)
            self.image = self.punchFrames[frame]
            self.image = pygame.transform.scale(self.image, (150, 150))



def superman_health():
    pygame.draw.rect(screen,(255,0,0),[1000,10,180,20])
def batman_health():
    pygame.draw.rect(screen, (255, 0, 0), [10, 10, 180, 20])


batman = pygame.image.load("batman.png")
superman=pygame.image.load("superman.png")
player=Player()
enemy=Enemy()
all_sprites = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
laserGroup = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
playerGroup.add(player)
enemyGroup.add(enemy)
FPS=100
clock=pygame.time.Clock()
Image=pygame.image.load('ghost_groung.png')
Image=pygame.transform.scale(Image,(1200,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    hit=pygame.sprite.groupcollide(playerGroup,enemyGroup,False,False)

    hit_2=pygame.sprite.groupcollide(playerGroup,laserGroup,False,True)

    if hit:

        if player.flyingKick:
            print("MARA")
            enemy.fall=True
        elif enemy.punch:
            player.fall=True
        elif player.punch:
            enemy.hurt=True
        else:
            enemy.hurt=False


    if hit_2:
        if player.stand or player.move_right or player.move_left or player.flyingKick:
            player.fall=True


    # screen.blit(Image,(0,0))
    screen.fill(white)

    all_sprites.draw(screen)
    all_sprites.update()
    superman_health()
    batman_health()
    pygame.display.update()
    clock.tick(FPS)
