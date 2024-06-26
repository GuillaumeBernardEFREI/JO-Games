import pygame
from math import *
import shooting.ran_gen as rg
import generic_classes as gc

class UFO(gc.General_Game_Object):
    def __init__(self,img_path):
        gc.General_Game_Object.__init__(self,img_path)
        #to define the variables and not have errors.
        self.x=-100
        self.y=-100
        

    def gen_traj(self,scr_size:pygame.rect) -> None:
        param=rg.gen_eq(scr_size)
        acc=1
        self.traj=Trajectory(False,param[0],param[1],acc*param[2],startpos=param[3])
        self.time=0

    def move(self,fps:int,screen_size:pygame.rect) -> None:
        self.time+=1/fps
        self.x,self.y=self.traj.position(self.time,True,screen_size)

    def draw(self,screen:gc.Screen) -> None:
        screen.blit(self.sprite,[self.x,self.y])

    def check(self,scr_size:pygame.rect) -> bool:
        if not (-100<self.x<scr_size.right): return True
        if not (-100<self.y<scr_size.bottom): return True
        return False
    
    def check_click(self) -> bool:
        mouse_pos=pygame.mouse.get_pos()
        if (pygame.mouse.get_pressed()[0]) and (mouse_pos[0]-self.x)<75 and (mouse_pos[1]-self.y)<75: 
            return True
        return False


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

    def position(self,time,fixed:bool=False,screen_size:tuple=None) -> list:
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
    
    def trajectory(self,nbpoints:int,starttime=0,maxtime=60,fixed:bool=False,screen_size:tuple=None)-> list[list]:
        #maxtime is in seconds
        values=list()
        for i in range(starttime,nbpoints+1): #from time=0 to time=maxtime 
            time=i*maxtime/nbpoints
            pos=self.position(time,fixed,screen_size)
            values.append(pos)
        return values