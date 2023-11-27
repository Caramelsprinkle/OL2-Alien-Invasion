import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, alienInvasionGame) -> None:
        super().__init__()
        self.screen = alienInvasionGame.screen
        self.settings = alienInvasionGame.settings
        self.color = self.settings.bulletColor
        self.rectangle = pygame.Rect(0, 0, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rectangle.midtop = alienInvasionGame.ship.rectangle.midtop
        self.y = float(self.rectangle.y)
        
    def update(self):
        self.y -= self.settings.bulletSpeed
        self.rectangle.y = self.y
        
    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rectangle)