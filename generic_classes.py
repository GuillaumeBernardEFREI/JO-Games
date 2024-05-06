import pygame as pg

class Screen(pg.Surface):
    def __init__(self,size:tuple[int,int],title):
        pg.Surface.__init__(self,size) #Remove error: 'pygame.error: display Surface quit'
        self.win=pg.display.set_mode(size,pg.RESIZABLE)
        self.win.fill((0,0,0))
        pg.display.set_caption(title)

    def rename(self,title:str) -> None:
        pg.display.set_caption(title)

    def update(self):
        pg.display.update()

class Background(pg.sprite.Sprite):
    def __init__(self,path):
        pg.sprite.Sprite.__init__(self)
        self.BG=pg.image.load(path).convert()

class General_Game_Object(pg.sprite.Sprite):
    def __init__(self,img_path, *args, **kargs):#*args and **kargs are if you don't want to have these values in all the classes but only in some that you created.
        pg.sprite.Sprite.__init__(self)
        self.path=img_path
        self.sprite=pg.image.load(self.path).convert_alpha()#The convert alpha should make the transparent pixels in png really transparent in pygame.
        if "resize" in kargs:
            self.resize(kargs['resize'])

    def resize(self,values:tuple[float,float]):
        self.sprite = pg.transform.scale(pg.image.load(self.path).convert_alpha(),values)
        #recreates the sprite at full quality and then scales it to the right value.

    def rect(self) -> pg.rect:
        return self.sprite.get_rect()
    #rect is the position of the sprite.