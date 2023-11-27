# the page is page 265 on the free pdf version at
# https://edu.anarcho-copy.org/Programming%20Languages/Python/Python%20Crash%20Course,%202nd%20Edition.pdf
# in case I accidentally press 'tab' and scroll al the way up, AGAIN

import sys
import pygame
from Settings import Settings
from Ship import Ship

"""Alien -> 🐢"""
class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Using Snake Case instead of Camel Case, I'm crying right now
        pygame.display.set_caption("Alien Invasion") # Using Snake Case for Pygame in Python based of real life pythons
        
        self.ship = Ship(self) # Maybe the true ship were the Ships inside us all along 🐑
        
        self.bg_color = (126, 87, 194) # Ah yes, blue screen color
        
    def runGame(self): 
        while True:
            self._checkEvents()
            self.ship.update()
            self._updateScreen()
        
    def _checkEvents(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit # no wait, come back!
                elif event.type == pygame.KEYDOWN:
                    self._checkKeyDownEvents(event)
                elif event.type == pygame.KEYUP:
                    self._checkKeyUpEvents(event)
    
    def _checkKeyDownEvents(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = True
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _checkKeyUpEvents(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = False
    
    def _updateScreen(self):
        self.screen.fill(self.settings.screen_height)
        self.ship.blitme()
            
        pygame.display.flip() # of the back variety
    # but actually though, why is it named 'flip'? out of all the names it could've used, maybe like 'update', why flip?

if __name__ == "__main__":
    alienInvasion = AlienInvasion()
    alienInvasion.runGame() # Your game is running? you better catch it before it gets too far