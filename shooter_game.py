#Создай собственный Шутер!
from pygame import *

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
    
window = display.set_mode((700, 500))
display.set_caption('Шутер')

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

player = Player('rocket.png', 5, 400, 80, 100, 10)
enemy = GameSprite('ufo.png', 600, 100, 80, 50, 10)

clock = time.Clock()

while True:

    for e in event.get():
        if e.type == QUIT:
            quit()

    window.blit(background, (0, 0))
    player.reset()
    enemy.reset()

    player.update()

    display.update()
    clock.tick(60)
