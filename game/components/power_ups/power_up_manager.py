import pygame
import random

from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD
from game.components.power_ups.drill_bullet import DrillBullet
from game.components.power_ups.quick_shot import QuickShot

MIN_SECONDS = 5000
MAX_SECONDS = 10000
class PowerUpManager:
    def __init__(self):
      self.power_ups = []
      self.when_appears = random.randint(MIN_SECONDS, MAX_SECONDS)
      self.duration = random.randint(3, 5)

    def generate_power_up(self):
       power_choice = random.choice(["shield", "drill ammo", "quick shot"])
       if power_choice == "drill ammo":
          power_up = DrillBullet()
       elif power_choice == "shield":
          power_up = Shield()
       elif power_choice == "quick shot":
          power_up = QuickShot()
          
       self.when_appears += random.randint(MIN_SECONDS, MAX_SECONDS)
       self.power_ups.append(power_up) 
      
    def update(self, game):
      current_time = pygame.time.get_ticks()

      if len(self.power_ups) == 0 and current_time >= self.when_appears:
         self.generate_power_up()

      for power_up in self.power_ups:
         if power_up.type == "shield":
           self.use_shield(game, power_up)
         elif power_up.type == "drill ammo":
            self.use_drill_bullets(game, power_up)
         elif power_up.type == "quick shot":
            self.use_speed_bullets(game, power_up)

    def use_shield(self, game, power_up):
      for power_up in self.power_ups:
         power_up.update(game.game_speed, self.power_ups)
         if game.player.rect.colliderect(power_up.rect):
           power_up.start_time = pygame.time.get_ticks()
           game.player.power_up_type = power_up.type
           game.player.has_power_up = True
           game.player.power_time_up = power_up.start_time + (self.duration * 1000)
           game.player.set_image((65, 75), SPACESHIP_SHIELD)
           self.power_ups.remove(power_up)
         
    def use_drill_bullets(self, game, power_up):
       for power_up in self.power_ups:
         power_up.update(game.game_speed, self.power_ups)
         if game.player.rect.colliderect(power_up.rect):
           power_up.start_time = pygame.time.get_ticks()
           game.player.power_up_type = power_up.type
           game.player.has_second_power_up = True
           game.player.power_time_up = power_up.start_time + (self.duration * 1000)
           self.power_ups.remove(power_up)

    def use_speed_bullets(self, game, power_up):
       for power_up in self.power_ups:
         power_up.update(game.game_speed, self.power_ups)
         if game.player.rect.colliderect(power_up.rect):
           power_up.start_time = pygame.time.get_ticks()
           game.player.power_up_type = power_up.type
           game.player.has_third_power_up = True
           game.player.power_time_up = power_up.start_time + (self.duration * 1000)
           self.power_ups.remove(power_up)
       
    def draw(self, screen):
      for power_up in self.power_ups:
        power_up.draw(screen)
      
    def reset(self):
       self.power_ups = []
       now = pygame.time.get_ticks()
       self.when_appears = random.randint(now + 5000, now +10000)