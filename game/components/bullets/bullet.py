import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, DRILL_BULLET_AMMO

class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET, (15, 25))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 20
    OWN_SPEED = 15

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type


    def update(self, bullets, game):
        if self.owner == 'player':
          self.rect.y -= self.OWN_SPEED
          if game.player.has_second_power_up:
            self.rect.y -= self.OWN_SPEED//2
            self.image = pygame.transform.scale(DRILL_BULLET_AMMO, (100, 100))
            self.rect = self.image.get_rect(center=self.rect.center)
          elif game.player.has_third_power_up:
              self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED

        if self.rect.y >= SCREEN_HEIGHT or self.rect.y <= 0:
            bullets.remove(self)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
