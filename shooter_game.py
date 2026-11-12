#Создай собственный Шутер!
#len ФУНКЦИЯ ДЛЯ ИЗМЕРЕНИЯ ДЛИННЫ СПИСКА
from pygame import *
from random import randint

win_width = 800
win_height = 600
lost = 0
dizlost = 0
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
clock = time.Clock()
life = 30
font.init()
font1 = font.Font(None, 80)
win = font1.render('5+', True, (0, 255, 0))
lose = font1.render('ВСЁ ПРОСРАНО!', True, (255, 0, 0))
font2 = font.Font(None, 50)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)
xx = mixer.Sound('fire.ogg')
xx.set_volume(0.2)

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):

   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed

   def fire(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            kayo = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
            kayo.add(isuzu)
            xx.play()

class Enemy(GameSprite):
   def update(self):
       self.rect.y += self.speed
       global lost

       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           lost = lost + 1

class Bullet(GameSprite):
   def update(self):
       self.reset()
       self.rect.y += self.speed
       if self.rect.y < 0:
           self.kill()




daf = Player('rocket.png', 5, win_height - 100, 80, 100, 10)

shinkansen = sprite.Group()
vva1 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
vva2 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
vva3 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
vva4 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
vva5 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
shinkansen.add(vva1)
shinkansen.add(vva2)
shinkansen.add(vva3)
shinkansen.add(vva4)
shinkansen.add(vva5)

isuzu = sprite.Group()
finish = True

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == True:
        sprites_list = sprite.spritecollide(daf, shinkansen, True)
        group_list = sprite.groupcollide(shinkansen, isuzu, True, True)
        if len(group_list) > 0:
            tbs = group_list
            nbs = len(tbs)
            for i in range(nbs):
                dizlost = dizlost + 1
                vva6 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
                shinkansen.add(vva6)
        if len(sprites_list) > 0:
            life = life - 1
            vva7 = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            shinkansen.add(vva7)
        window.blit(background,(0,0))
        if dizlost >= 100:
            finish = False
            window.blit(win,(250, 180))
        if life <= 0:
            finish = False
            window.blit(lose,(250, 180))
        if lost >= 30:
            finish = False
            window.blit(lose, (200, 180))
        text_lose = font2.render("ПРОПУЩЕНО: " + str(lost), 1, (255, 0, 0))
        text_win = font2.render('ОБНУЛЕНО:' + str(dizlost), 1, (0, 255, 0))
        text_wl = font2.render('ЖИЗНИ:' + str(life), 1, (0, 0, 255))
        daf.update()
        shinkansen.update()
        window.blit(text_lose, (5,5))
        window.blit(text_win, (525,5))
        window.blit(text_wl, (325, 5))
        daf.reset()
        shinkansen.draw(window)
        shinkansen.update()
        daf.fire()
        isuzu.update()
    display.update()
    clock.tick(40)
/Users/mac/VSCode/code-portable-data/extensions/algovscode.algoritmika-python-20250904.95201.0/data/student/70130557/657891