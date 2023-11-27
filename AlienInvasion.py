# the page is page 265 on the free pdf version at
# https://edu.anarcho-copy.org/Programming%20Languages/Python/Python%20Crash%20Course,%202nd%20Edition.pdf
# in case I accidentally press 'tab' and scroll al the way up, AGAIN

import sys
import pygame
from Settings import Settings
from Ship import Ship
from Bullet import Bullet
from Alien import Alien

"""Alien -> 🐢"""
class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._createFleet()
        
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) Not making it fullscreen
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight)) # Using Snake Case instead of Camel Case, I'm crying right now
        pygame.display.set_caption("Alien Invasion") # Using Snake Case for Pygame in Python based of real life pythons
        
        self.ship = Ship(self) # Maybe the true ship were the Ships inside us all along 🐑
        
        self.bg_color = (126, 87, 194) # Ah yes, blue screen color
        
    def runGame(self) -> None: # I'm too tired to write anymore comments..
        while True: # Why is one chapter so longgggg
            self._checkEvents()
            self.ship.update()
            self._updateBullets()
            self._updateScreen()
        
    def _checkEvents(self) -> None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit # no wait, come back!
                elif event.type == pygame.KEYDOWN:
                    self._checkKeyDownEvents(event)
                elif event.type == pygame.KEYUP:
                    self._checkKeyUpEvents(event)
    
    def _checkKeyDownEvents(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fireBullet()
            
    def _checkKeyUpEvents(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = False
    
    def _updateBullets(self) -> None:
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rectangle.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
    
    def _fireBullet(self) -> None:
        if len(self.bullets) < self.settings.bulletsAllowed:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
    
    def _createFleet(self) -> None:
        alien = Alien(self)
        alienWidth = alien.rect.width
        availableSpaceRow = self.settings.screenWidth - (2 * alienWidth)
        alienNumberInRow = availableSpaceRow // (2 * alienWidth)
        for alienIndex in range(alienNumberInRow):
            self._createAlien(alienIndex)
    
    def _createAlien(self, alienIndex) -> None:
        alien = Alien(self)
        alienWidth = alien.rect.width
        alien.x = alienWidth + 2 * alienWidth * alienIndex
        alien.rect.x = alien.x
        self.aliens.add(alien)
    
    def _updateScreen(self) -> None:
        self.screen.fill(self.settings.screenHeight)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        self.aliens.draw(self.screen)
            
        pygame.display.flip() # of the back variety
    # but actually though, why is it named 'flip'? out of all the names it could've used, maybe like 'update', why flip?

if __name__ == "__main__":
    alienInvasion = AlienInvasion()
    alienInvasion.runGame() # Your game is running? you better catch it before it gets too far