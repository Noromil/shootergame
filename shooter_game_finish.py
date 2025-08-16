from pygame import *
from random import randint
from time import sleep
from pygame.sprite import spritecollide

windows = display.set_mode((640,480))

background = transform.scale(image.load("galaxy.jpg") , (640 , 480))
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
mixer.music.set_volume(0.01)



class GameSprite(sprite.Sprite):
    # konstruktor ke
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

kumpulanpeluru = sprite.Group()


class player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys [K_RIGHT]:
            self.rect.x += 5
    def fire(self):
        keys1 = key.get_pressed()

        if keys1[K_e]:
            peluru = bullet('bullet.png' , self.rect.centerx , self.rect.centery , 5 )
            kumpulanpeluru.add(peluru)



lost = 0
score = 0

class enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y  >=480:
           self.rect.y = 0
           global lost
           self.rect.x = randint(0, 640)
           lost = lost +1

class bullet(GameSprite):
    def update(self):
        self.rect.y -= 10
        if self.rect.y <= 0 :
            self.kill()


inidmorbullet = bullet('bullet.png' , 300 , 300 , 2)


musuh = enemy ('ufo.png' , randint(0 , 640) , 0 , randint(5 , 10) )
musuh2 = enemy ('ufo.png' , randint(0 , 640) , 0 , randint (5 , 10))
musuh3 = enemy ('ufo.png' , randint(0 , 640) , 0 , randint (5 , 10) )
musuh4 = enemy ('ufo.png' , randint(0 , 640) , 0 ,randint (5 , 10) )
musuh5 = enemy ('ufo.png' , randint(0 , 640) , 0 , randint (5 , 10)  )



sirkelmusuh = sprite.Group()
sirkelmusuh.add(musuh)
sirkelmusuh.add(musuh2)
sirkelmusuh.add(musuh3)
sirkelmusuh.add(musuh4)
sirkelmusuh.add(musuh5)


asteroid = enemy('asteroid.png' , randint(0 , 640) , 0 ,randint(3 , 5))
asteroid2 = enemy('asteroid.png' , randint(0 , 640) , 0 ,randint(3 , 5))
asteroid3 = enemy('asteroid.png' , randint(0 , 640) , 0 ,randint(3 , 5))

sirkelasteroid = sprite.Group()
sirkelasteroid.add(asteroid)
sirkelasteroid.add(asteroid2)
sirkelasteroid.add(asteroid3)



pemain = player('rocket.png' , 20 , 400 , 3)










game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 36)


while game:




    sprite_nabrak = sprite.groupcollide(kumpulanpeluru , sirkelmusuh , True , True)
    for monster in sprite_nabrak :
        rawr = enemy('ufo.png' , randint(0 , 640) , 0 , randint(5 , 10))
        sirkelmusuh.add(rawr)
        score = score +1
    if score == 50:
        menang = font1.render(
            "You Win" , 1 , (253 ,206 , 15)
        )
        windows.blit(menang , (250 , 200))
        display.update()
        sleep(8)
        game = False

    if lost == 100:
        kalah2 = font1.render(
            "you lost" , 1 , (253 , 21 , 21)
        )
        windows.blit(kalah2 , (250 ,200))
        display.update()
        sleep(7)
        game = False

    esteh = sprite.spritecollide(pemain, sirkelasteroid , True)
    if esteh:
        skibididopdop = font1.render(
            "GAME OVER", 1, (253, 21, 21))
        windows.blit(skibididopdop , (250 ,200))
        display.update()
        sleep(5)
        game = False





    kalah_p = sprite.spritecollide(pemain , sirkelmusuh , True  )
    if kalah_p:
            bob = font1.render(
                "GAME OVER" , 1, (253, 21, 21)
         )
            windows.blit(bob , (250, 200))
            display.update()
            sleep(6)
            game = False


    text_lose = font1.render(
        "Missed : " + str(lost), 1, (255, 255, 255)
    )
    scoreg = font1.render(
        "Score :" + str(score) , 1 , (255, 255, 255)
    )
    for e in event.get():
        if e.type == QUIT:
            game = False
    windows.blit(background , (0 , 0 ))
    windows.blit(text_lose , (0 , 0))
    windows.blit(scoreg , (0 , 30))
    pemain.reset()
    pemain.update()
    pemain.fire()
    kumpulanpeluru.draw(windows)
    kumpulanpeluru.update()
    sirkelasteroid.draw(windows)
    sirkelasteroid.update()
    sirkelmusuh.draw(windows)
    sirkelmusuh.update()
    inidmorbullet.update()
    inidmorbullet.reset()
    clock.tick(40)
    display.update()



















