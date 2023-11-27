import pygame

class Ship:
    def __init__(self, alienInvasionGame) -> None: # ai? what's ai? Artificial Intelligence? This must be the artificial intelligence game
        self.screen = alienInvasionGame.screen
        self.settings = alienInvasionGame.settings
        self.screenRectangle = alienInvasionGame.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rectangle = self.image.get_rect() # get rectangle? that's pretty rude
        
        self.rectangle.midbottom = self.screenRectangle.midbottom
        
        self.x = float(self.rectangle.x)
        
        self.movingLeft = False
        self.movingRight = False
    
    def update(self):
        if self.movingRight and self.rectangle.right < self.screenRectangle.right:
            self.x += self.settings.shipSpeed
        if self.movingLeft and self.rectangle.left > 0:
            self.x -= self.settings.shipSpeed
            
        self.rectangle.x = self.x
    
    def blitme(self): # def: bit blit = Bit blit is a data operation commonly used in computer graphics in which several bitmaps are combined into one using a boolean function.
        self.screen.blit(self.image, self.rectangle) # coulda just called it draw 🐢🐢🐢
        