from Goodminton import *

class Screen(pygame.Surface):
    def __init__(self):
        size=1450,840
        pygame.Surface.__init__(self,size)
        self.screen=pygame.display.set_mode(size)

class Background(pygame.sprite.Sprite):
    def __init__(self,path):
            pygame.sprite.Sprite.__init__(self)
            self.BD=pygame.image.load(path).convert()

class General_Game_Object(pygame.sprite.Sprite):
    def __init__(self,img_path, *args, **kargs):#*args and **kargs are if you don't want to have these values in all the classes but only in some that you created.
        pygame.sprite.Sprite.__init__(self)
        self.sprite=pygame.image.load(img_path).convert_alpha()#The convert alpha should make the transparent pixels in png really transparent in pygame.
        if "resize" in kargs:
            self.resize(kargs['resize'])


    def resize(self,values):
        self.sprite = pygame.transform.scale(self.sprite,values)

    def rect(self):
        return self.sprite.get_rect()
    #rect is the position of the sprite.


class player(General_Game_Object):
    def __init__(self ,img_path, *args, **kargs):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(img_path, *args, **kargs)

    def












