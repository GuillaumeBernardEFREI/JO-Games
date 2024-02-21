from math import *
class Vector2:
    def __eq__(self,u)->bool:
        return (self.x==u.x and self.y==u.y)
    def __repr__(self)->str:
        return "[ "+str(self.x)+" , "+str(self.y)+" ]"
    def __init__(self,x=0.0,y=0.0):
        self.x,self.y =x,y
    def __str__(self)->str:
        return "[ "+str(self.x)+" , "+str(self.y)+" ]"
    def __add__(self,u):
        # u must be a Vector2, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x+u.x,self.y+u.y)
        return Vector2(self.x+u,self.y+u)
    def __sub__(self,u):
        # u must be a Vector3, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x-u.x,self.y-u.y)
        return Vector2(self.x-u,self.y-u)
    def __truediv__(self,u):
        # u must be a Vector3, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x/u.x,self.y/u.y)
        return Vector2(self.x/u,self.y/u)
    def __mul__(self,u):
        # u must be a Vector3, interger or a float/int
        if isinstance(u,Vector2):
            return Vector2(self.x*u.x,self.y*u.y)
        return Vector2(self.x*u,self.y*u)
    def frac(self):
        return Vector2(self.x%1,self.y%1)
    def rotate(self,rotation):
        #https://en.wikipedia.org/wiki/Rotation_matrix
        rotation *= (pi/180)

        return Vector2()
    def normalize(self):
        # normalize the vector (self**2 =1)
        d = sqrt(self.x**2+self.y**2)
        return Vector2(self.x/d,self.y/d)
    def norm(self) -> float:
        # normalize the vector (self**2 =1)
        d = sqrt(self.x**2+self.y**2)
        return d
    def _fabs(self):
        return Vector2(fabs(self.x),fabs(self.y))
    def dotProduct(self,u,isAbs=False)->float:
        #return the dot product of 2 vector2
        if not isAbs:
            return self.x*u.x+self.y*u.y
        return fabs(self.x*u.x)+fabs(self.y*u.y)
    def _sum(self)->float:
        # return the sum of x and y
        return self.x+self.y
    def distance(self,u,doSqrt)->float:
        # return the distance between two points
        # doSqrt=True -> use square root
        # else return square distance
        if doSqrt:
            return sqrt(((self-u)*(self-u))._sum())
        return ((self-u)*(self-u))._sum()
    
class Trajectory:
    def __init__(self,use_velocity_vector:bool,launchvelocity:float,angleoflaunch:float,aceleration:float=9.81,start_velocity:Vector2=Vector2(1,1),startpos:Vector2=Vector2(0,0)) -> None:
        if use_velocity_vector:
            self.a=aceleration/2 #the value should be negative to have
            self.b=start_velocity.norm()

            self.ax=0 #The acceleration will only be the downward gravity for the moment (simplicity to understand)
            self.bx=start_velocity.x

            self.ay=aceleration/2
            self.by=start_velocity.y
        else:
            self.a=aceleration/2
            self.b=launchvelocity

            #because we use an euclidian system, we can consider the values beeing one of a right triangle.
            self.ax=0
            self.bx=launchvelocity*sin(angleoflaunch) #values are in radians

            self.ay=aceleration/2
            self.by=launchvelocity*cos(angleoflaunch) #angleoflaunch is in radians!

        self.c=startpos.norm()
        self.cx=startpos.x
        self.cy=startpos.y
        
        self.equation=f"{self.a}t^2+{self.b}t+{self.c}" #the equation is of the form ax^2+bx+c
                                # And the equation of this particular is stored into this string variable.
                                #this equation is only to be displayed in dev menus not to be used (i need to check if it even is correct)

        self.startpos=startpos

    #    x = horizontal motion
    #    y = vertical motion
    def position(self,time,fixed:bool=False,screen_size:tuple|None=None) -> tuple:
        x=self.ax*(time**2)+self.bx*time
        y=self.ay*(time**2)+self.by*time
        #Be careful in case you wish to use the fixed function, you will need to move the start of the equation or use the method : Fixed_Startpos (to be called on every resize of the screen)
        if fixed: #The equation will be fixed to be calculated in a 10k*10k radius (only positive)
                # And then we render it down to the size of the screen, done here.
            if screen_size==None:
                raise TypeError("You need to give the screen size to make the equation a fixed one.")
            x*=screen_size[2]/10000 #screen size is the rect of the screen.
            y*=screen_size[3]/10000
        
        x+=self.cx
        y+=self.cy
        return (x,y) #sadly, we cannot output a vector2 because it won't work with pygame.

    def trajectory(self,nbpoints:int,starttime=0,maxtime=60,fixed:bool=False,screen_size:tuple|None=None)-> list[Vector2]:
        #maxtime is in seconds
        values=list()
        for i in range(starttime,nbpoints+1): #from time=0 to time=maxtime 
            time=i*maxtime/nbpoints
            pos=self.position(time,fixed,screen_size)
            values.append(pos)
        return values
    
    #def Fixed_Startpos(self,screen_size):
