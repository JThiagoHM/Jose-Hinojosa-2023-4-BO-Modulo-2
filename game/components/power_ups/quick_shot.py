import random

from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPEED_BULLET,SPEED_BULLET_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT


class QuickShot(PowerUp):
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self, move_x_for = [30, 100]):
      super().__init__(SPEED_BULLET ,SPEED_BULLET_TYPE) 
      self.rect.x = random.randint(120, SCREEN_HEIGHT - 200)
      self.rect.y = 0
      self.movement_x = self.MOV_X[random.randint(0, 1)]
      self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
      self.index = 0
      
    def update(self, game_speed, power_ups):
      self.rect.y += game_speed -5
      if self.movement_x == 'left':
        self.rect.x -= game_speed
      else:
        self.rect.x += game_speed
      self.change_movement_x()

      if self.rect.y >= SCREEN_HEIGHT:
        power_ups.remove(self)

    def change_movement_x(self):
      self.index +=1
      if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH):
        self.movement_x = 'left'
        self.index = 0 
      elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
        self.movement_x = 'right'
        self.index = 0 