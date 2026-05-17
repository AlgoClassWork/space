#Создай собственный Шутер!
from random import randint
from pygame import *

score = 0
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 615:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            lost += 1
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    
window = display.set_mode((700, 500))
display.set_caption('Шутер')

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

player = Player('rocket.png', 5, 400, 80, 100, 10)

bullets = sprite.Group()

enemys = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(80, 620), -40, 80, 50, randint(1, 5))
    enemys.add(enemy)

font.init()
my_font = font.SysFont('Arial', 36)


clock = time.Clock()

while True:

    for e in event.get():
        if e.type == QUIT:
            quit()
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    score_text = my_font.render('Счет: ' + str(score), True, (255, 255, 255))
    lost_text = my_font.render('Пропущено: ' + str(lost), True, (255, 255, 255))

    window.blit(background, (0, 0))
    window.blit(score_text, (10, 10))
    window.blit(lost_text, (10, 40))

    player.reset()
    enemys.draw(window)
    bullets.draw(window)

    player.update()
    enemys.update()
    bullets.update()


    if sprite.spritecollide(player, enemys, False):
        print('Ты проиграл!')


    if sprite.groupcollide(enemys, bullets, True, True):
        enemy = Enemy('ufo.png', randint(80, 620), -40, 80, 50, randint(1, 5))
        enemys.add(enemy)
        score += 1
        

    display.update()
    clock.tick(60)
