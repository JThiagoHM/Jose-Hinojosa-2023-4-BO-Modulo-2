import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHOOT_SOUND
from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):

   SHIP_WIDTH = 40 
   SHIP_HEIGHT = 60
   X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
   Y_POS = 500
   SHIP_SPEED = 10

   def __init__(self):
       self.image = SPACESHIP
       self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
       self.rect = self.image.get_rect()
       self.rect.x = self.X_POS
       self.rect.y = self.Y_POS
       self.type = 'player'

   def update(self, user_input, game):
       if user_input[pygame.K_UP] and user_input[pygame.K_RIGHT]:
          self.move_up()
          self.move_right()
       elif user_input[pygame.K_UP] and user_input[pygame.K_LEFT]:
         self.move_up()
         self.move_left()
       elif user_input[pygame.K_DOWN] and user_input[pygame.K_RIGHT]:
         self.move_down()
         self.move_right()
       elif user_input[pygame.K_DOWN] and user_input[pygame.K_LEFT]:
         self.move_down()
         self.move_left()
        
       elif user_input[pygame.K_LEFT]:
         self.move_left()
         if user_input[pygame.K_LEFT] and user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

       elif user_input[pygame.K_RIGHT]:
         self.move_right()
         if user_input[pygame.K_RIGHT] and user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

       elif user_input[pygame.K_UP]:
         self.move_up()
         if user_input[pygame.K_UP] and user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

       elif user_input[pygame.K_DOWN]:
         self.move_down()
         if user_input[pygame.K_DOWN] and user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

       elif user_input[pygame.K_SPACE]:
         self.shoot(game.bullet_manager)
      
   def move_left(self):
      self.rect.x -= self.SHIP_SPEED
      if self.rect.left < 0:
        self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

   def move_right(self):
      self.rect.x += self.SHIP_SPEED
      if self.rect.right >= SCREEN_WIDTH - self.SHIP_HEIGHT:
        self.rect.x = 0
    
   def move_up(self):
       if self.rect.y > SCREEN_HEIGHT // 2:
         self.rect.y -= self.SHIP_SPEED

   def move_down(self):
       if self.rect.y < SCREEN_HEIGHT - 70:
         self.rect.y += self.SHIP_SPEED

   #def move_up_right(self): 
    #   self.move_right()
     #  self.move_up()

   # def move_up_left(self): 
   #    if self.rect.y > SCREEN_HEIGHT // 2 and self.rect.left >= 0:
   #      self.rect.y -= self.SHIP_SPEED
   #     self.rect.x -= self.SHIP_SPEED 
   #    elif self.rect.left < 0:
   #     self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH
            
   #def move_down_right(self): 
   #    if self.rect.y < SCREEN_HEIGHT - 70 and self.rect.right <= SCREEN_WIDTH:
   #      self.rect.y += self.SHIP_SPEED
   #      self.rect.x += self.SHIP_SPEED
   #    elif self.rect.right >= SCREEN_WIDTH - self.SHIP_HEIGHT:
   #      self.rect.x = 0
    #def move_down_left(self): 
    #  if self.rect.y < SCREEN_HEIGHT - 70 and self.rect.left >= 0:
    #     self.rect.y += self.SHIP_SPEED
    #     self.rect.x -= self.SHIP_SPEED
    #  elif self.rect.left < 0:
    #    self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

   def draw(self, screen):
       screen.blit(self.image, (self.rect.x, self.rect.y)) 

   def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
        SHOOT_SOUND.play()

        
        
