import pygame

from game.utils.constants import GAME_OVER_SOUND
from game.utils.constants import SHIELD_TYPE, DRILL_BULLET_TYPE

class BulletManager:
  def __init__(self):
    self.bullets = []
    self.enemy_bullets = []

  def update(self, game):
   for bullet in self.enemy_bullets:
      bullet.update(self.enemy_bullets, game)

      if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
        self.enemy_bullets.remove(bullet)
        if game.player.power_up_type != SHIELD_TYPE:
          GAME_OVER_SOUND.play()
          game.death_count += 1
          game.playing = False
          pygame.time.delay(2000)
          break

   for bullet in self.bullets:
      bullet.update(self.bullets, game)
      for enemy in game.enemy_manager.enemies:
       if game.player.power_up_type == DRILL_BULLET_TYPE and (bullet.rect.colliderect(enemy) and bullet.owner == 'player'):
           game.enemy_manager.enemies.remove(enemy)
       elif bullet.rect.colliderect(enemy) and bullet.owner == 'player':
        self.bullets.remove(bullet)
        game.enemy_manager.enemies.remove(enemy)
        game.update_score()
      

  def draw(self, screen):
    for bullet in self.enemy_bullets:
        bullet.draw(screen)

    for bullet in self.bullets:
        bullet.draw(screen)

  def add_bullet(self, bullet):
    if bullet.owner == 'enemy' and len(self.enemy_bullets) <=1:
      self.enemy_bullets.append(bullet)
      pass
    elif bullet.owner == 'player' and len(self.bullets) <3:
      self.bullets.append(bullet)
 
  def reset(self):
     self.bullets = []
     self.enemy_bullets = []
   