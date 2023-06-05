import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2 

    def __init__(self, screen):
      screen.fill((255, 255, 255))
      self.font = pygame.font.Font(FONT_STYLE, 30)

    def update(self, game):
       pygame.display.update()
       self.handle_events_on_menu(game)
    
    def draw(self, screen):
       screen.blit(self.text, self.text_rect)

    def handle_events_on_menu(self, game):
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             game.playing = False
             game.running = False
          elif event.type == pygame.KEYDOWN:
             game.run()

    def reset_screen_color(self, screen):
       screen.fill((255, 255, 255))

    def update_message(self, screen, message, scores, height_size, color):
        self.text = self.font.render(f'{message} {scores}', True, color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH , self.HALF_SCREEN_HEIGHT + height_size)
        screen.blit(self.text, self.text_rect)

    #def draw(self, screen, message, x = 550, y = 50, color = (255, 255, 255)):
     #  text = self.font.render(message, True, color)
      # text_rect = text.get_rect()
      # text_rect.center = (x, y)
      # screen.blit(text, text_rect)