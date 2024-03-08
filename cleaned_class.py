import pygame
from math import *

class Screen(pygame.Surface):
    def __init__(self):
        size=420,420
        pygame.Surface.__init__(self,size)
        self.screen=pygame.display.set_mode(size,pygame.locals.RESIZABLE)


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


class Trajectory:
    def __init__(self,use_velocity_vector:bool,launchvelocity:float,angleoflaunch:float,aceleration:float=9.81,start_velocity:tuple=(1,1),startpos:tuple=(0,0)) -> None:
        if use_velocity_vector:
            self.launchvelo=sqrt(start_velocity[0]**2+start_velocity[1]**2) # pythagoras
            self.ax=0 #The acceleration will only be the downward gravity for the moment (simplicity to understand)
            self.bx=start_velocity[0]

            self.ay=aceleration/2
            self.by=start_velocity[1]
        else:
            self.launchvelo=launchvelocity
            #because we use an euclidian system, we can consider the values beeing one of a right triangle.
            self.ax=0
            self.bx=launchvelocity*sin(angleoflaunch) #values are in radians

            self.ay=aceleration/2
            self.by=launchvelocity*cos(angleoflaunch) #angleoflaunch is in radians!

        self.cx=startpos[0]
        self.cy=startpos[1]

        #This equation represents y(x) and time has been eliminated.
        #The simplification is easy since we have chosen to have ax=0
        self.a=self.ay/(self.bx**2)
        self.b=-(2*self.ay)/(self.bx**2)      +self.by/(self.bx) #see calculations done on a sheet
        self.c=(self.ay*(self.cx**2))/(self.bx**2)    -(self.by*self.cx)/(self.bx)      +self.cy

        self.equation=f"y(x)={self.a:8f}x²+{self.b:8f}x+{self.c:8f}" #the equation is of the form ax^2+bx+c
                                # And the equation of this particular trajectory is stored into this string variable.
                                #this equation is only to be displayed in dev menus not to be used.
        self.startpos=startpos

    #    x = horizontal motion
    #    y = vertical motion

    def position(self,time,fixed:bool=False,screen_size:tuple|None=None) -> list:
        x=self.ax*(time**2)+self.bx*time
        y=self.ay*(time**2)+self.by*time
        if fixed: #The equation will be fixed to be calculated in a 10k*10k radius (only positive)
                # And then we render it down to the size of the screen, done here.
            if screen_size==None:
                raise TypeError("You need to give the screen size to make the equation a fixed one.")
            x*=screen_size[2]/10000 #screen size is the rect of the screen.
            y*=screen_size[3]/10000

        x+=self.cx
        y+=self.cy
        return [x,y]
    
    def trajectory(self,nbpoints:int,starttime=0,maxtime=60,fixed:bool=False,screen_size:tuple|None=None)-> list[list]:
        #maxtime is in seconds
        values=list()
        for i in range(starttime,nbpoints+1): #from time=0 to time=maxtime 
            time=i*maxtime/nbpoints
            pos=self.position(time,fixed,screen_size)
            values.append(pos)
        return values