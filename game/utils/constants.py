import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'

SHOOT_SOUND = pygame.mixer.Sound('game/assets/Sounds/DisparoNave.mp3')
ENEMY_SHOOT_SOUND = pygame.mixer.Sound('game/assets/Sounds/DisparoEnemigo.mp3')
GAME_OVER_SOUND = pygame.mixer.Sound('game/assets/Sounds/GAMEOVER.mp3') 
DRILL_BULLET = pygame.image.load(os.path.join(IMG_DIR, 'Bullet/BigBullet.png'))
DRILL_BULLET_TYPE = 'drill ammo'
DRILL_BULLET_AMMO = pygame.image.load(os.path.join(IMG_DIR, 'Bullet/DrillBullet.png'))
SPEED_BULLET = pygame.image.load(os.path.join(IMG_DIR, 'Bullet/SpeedBullet.png'))
SPEED_BULLET_TYPE = 'quick shot'


INIT_SOUND = pygame.mixer.Sound('game/assets/Sounds/InitSound.mp3')